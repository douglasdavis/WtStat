#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import

import sys
import os
import re
import math
from copy import deepcopy
from array import array
from collections import OrderedDict
import yaml
import logging

IN_ATLAS_RELEASE = "AnalysisTop_VERSION" in os.environ
if IN_ATLAS_RELEASE:
    import WtPyext.six as six
    from WtPyext.enum import Enum
    from WtStat.systematics import SYS_WEIGHTS, PDF_WEIGHTS
    if __name__ == "__main__":
        log = logging.getLogger("in_release-standalone-rdf_builder")
    else:
        log = logging.getLogger(__name__)

else:
    if sys.version_info.major == 2:
        print("Standalone mode requires python3")
        sys.exit(1)
    import six
    from enum import Enum
    logging.basicConfig(level=logging.INFO, format="{:15}  %(levelname)s  %(message)s".format("[%(name)s]"))
    logging.addLevelName(logging.WARNING, "\033[1;31m{:8}\033[1;0m".format(logging.getLevelName(logging.WARNING)))
    logging.addLevelName(logging.ERROR, "\033[1;35m{:8}\033[1;0m".format(logging.getLevelName(logging.ERROR)))
    logging.addLevelName(logging.INFO, "\033[1;32m{:8}\033[1;0m".format(logging.getLevelName(logging.INFO)))
    logging.addLevelName(logging.DEBUG, "\033[1;34m{:8}\033[1;0m".format(logging.getLevelName(logging.DEBUG)))
    log = logging.getLogger("standalone-rdf_builder")


# fmt: off
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
RDataFrame = ROOT.ROOT.RDataFrame
TH1DModel = ROOT.ROOT.RDF.TH1DModel
SaveGraph = ROOT.ROOT.RDF.SaveGraph
# fmt: on


class BinType(Enum):
    FIXED = 0
    VARIABLE = 1
    UNDEFINED = 99


class NtupleType(Enum):
    DATA = 0
    NOMINAL = 1
    SYSTEMATIC = 2
    UNDEFINED = 99


class NtupleDefinition(object):
    name = ""
    files = []
    ntype = NtupleType.UNDEFINED
    tree_systematic = None

    @property
    def tree_name(self):
        if self.tree_systematic is None:
            return "nominal"
        else:
            return self.tree_systematic

    def __repr__(self):
        return "<NtupleDefinition: {} {} {} {}>".format(
            self.name, self.files, self.ntype, self.tree_name
        )


class RegionDefinition(object):
    name = ""
    selection = ""
    bin_type = BinType.UNDEFINED
    binning = None
    nbins = 0
    xmin = 0
    xmax = 0

    def __repr__(self):
        if self.bin_type == BinType.FIXED:
            return "<RegionDefinition: {}, {}, {}, {}, {}>".format(
                self.name, self.selection, self.nbins, self.xmin, self.xmax
            )
        if self.bin_type == BinType.VARIABLE:
            return "<RegionDefinition: {}, {}, {}>".format(
                self.name, self.selection, self.binning
            )


class TemplateDefinition(object):
    var = ""
    weight = "weight_nominal"
    weight_suffix = None
    regions = []
    bin_type = BinType.UNDEFINED
    use_region_binning = False
    binning = None
    nbins = 0
    xmin = 0
    xmax = 0
    axis_title = "title"
    is_aux = True

    # fmt: off
    def __repr__(self):
        return "<TemplateDefinition: {}>".format(
            ", ".join([self.var, self.weight, str(self.weight_suffix), str(self.regions),
                       str(self.use_region_binning), str(self.binning), str(self.nbins),
                       str(self.xmin), str(self.xmax), self.axis_title, str(self.is_aux)]))
    # fmt: on


NOMINAL_REGEXES = {
    "ttbar": re.compile("ttbar_410472_FS"),
    "ttbar_AFII": re.compile("ttbar_410472_AFII"),
    "ttbar_RU_AFII": re.compile("ttbar_410482_AFII"),
    "ttbar_H7_AFII": re.compile("ttbar_410558_AFII"),
    "ttbar_MCaNLO_AFII": re.compile("ttbar_410465_AFII"),
    "tW": re.compile("tW_DR_41064(8|9)_FS"),
    "tW_AFII": re.compile("tW_DR_41064(8|9)_AFII"),
    "tW_DS_FS": re.compile("tW_DS_41065(6|7)_FS"),
    "tW_H7_AFII": re.compile("tW_DR_41103(8|9)_AFII"),
    "tW_MCaNLO_AFII": re.compile("tW_412003_AFII"),
}


def rdf_args(parser):
    parser.add_argument("-d", "--directory", type=str, required=True, help="directory containing Wt ROOT files")
    parser.add_argument("-c", "--config", type=str, default="auto", required=False, help="configuration file")
    parser.add_argument("-o", "--outfile", type=str, required=True, help="output file")
    parser.add_argument("--exclude-weights", type=str, nargs="+", default=[], help="set of weight systematics to exclude")
    parser.add_argument("--exclude-trees", type=str, nargs="+", default=[], help="set of tree systematics to exclude")
    parser.add_argument("--no-tree-systematics", dest="notreesys", action="store_true", help="ignore all tree  systematics")
    parser.add_argument("--no-weight-systematics", dest="noweightsys", action="store_true", help="ignore all weight systematics")
    parser.add_argument("--tree-prefix", type=str, default="WtLoop", help="Wt tree prefix (WtTMVA or WtLoop)")
    parser.add_argument("--disable-imt", action="store_true", help="disable ROOT's implicit multithreading")
    parser.add_argument("--debug", action="store_true", help="turn on debug statements")
    parser.add_argument("--do-aux", action="store_true", help="Do templates with aux property set to true in YAML config")
    parser.add_argument("--do-tiny", action="store_true", help="Do systematics labeled as tiny")
    parser.add_argument("--force-graph", action="store_true", help="force graph (somehow avoids crash with aux variables)")
    return 0


def sortfiles_nominal(file_list):
    """
    Given a list of files, sort them into a dictionary of {ntuple_title, file_list}
    """
    files = OrderedDict()
    for title in ["Data", "Diboson", "Zjets", "MCNP", "ttV"]:
        files[title] = []
    for title in NOMINAL_REGEXES:
        files[title] = []

    for f in file_list:
        if not f.endswith(".root"):
            continue
        if "nominal" not in f:
            continue
        if "MCNP" in f:
            files["MCNP"].append(f)
        elif "Data" in f:
            files["Data"].append(f)
        elif "Zjets" in f:
            files["Zjets"].append(f)
        elif "Diboson" in f:
            files["Diboson"].append(f)
        elif "ttV" in f:
            files["ttV"].append(f)

        elif "nominal" in f:
            for k, v in six.iteritems(NOMINAL_REGEXES):
                if v.search(f):
                    files[k].append(f)

    return files


def sortfiles_systematic(file_list, args):
    """
    Given a list of files, sort them into a dictionary of
    {(ntuple_title, sys_tree_name), file_list}
    """
    re_tW_sys_FS = re.compile("(tW_DR_[0-9]{6}_FS_MC16(a|d|e)_)")
    re_tt_sys_FS = re.compile("(ttbar_[0-9]{6}_FS_MC16(a|d|e)_)")
    files = OrderedDict()
    for f in file_list:
        if not f.endswith(".root"):
            continue
        if "nominal" in f:
            continue
        if not ("tW_DR" in f or "ttbar" in f):
            continue
        if "tW_DR" in f:
            sres = re_tW_sys_FS.search(f)
            if sres:
                sys_tree_name = f.split(sres.group(0))[-1].split(".")[0]
                if sys_tree_name in args.exclude_trees:
                    pass
                elif ("tW", sys_tree_name) not in files:
                    files[("tW", sys_tree_name)] = [f]
                else:
                    files[("tW", sys_tree_name)].append(f)
        if "ttbar" in f:
            sres = re_tt_sys_FS.search(f)
            if sres:
                sys_tree_name = f.split(sres.group(0))[-1].split(".")[0]
                if sys_tree_name in args.exclude_trees:
                    pass
                elif ("ttbar", sys_tree_name) not in files:
                    files[("ttbar", sys_tree_name)] = [f]
                else:
                    files[("ttbar", sys_tree_name)].append(f)
    return files


def region_definitions(yaml_config):
    region_defs = []
    for entry in yaml_config["regions"]:
        regdef = RegionDefinition()
        regdef.name = entry["name"]
        regdef.selection = entry["selection"]
        if "binning" in entry:
            regdef.bin_type = BinType.VARIABLE
            regdef.binning = array("d", entry["binning"])
        elif "nbins" in entry:
            regdef.bin_type = BinType.FIXED
            regdef.nbins = entry.get("nbins")
            regdef.xmin = entry.get("xmin")
            regdef.xmax = entry.get("xmax")
        else:
            regdef.bin_type = BinType.UNDEFINED
        region_defs.append(regdef)
    return region_defs


def template_definitions(yaml_config, args):
    template_defs = []
    all_regions = [entry["name"] for entry in yaml_config["regions"]]
    for entry in yaml_config["templates"]:
        tdef = TemplateDefinition()
        tdef.var = entry["var"]
        tdef.regions = entry["regions"]
        tdef.use_region_binning = entry["use_region_binning"]
        tdef.axis_title = entry["axis_title"]
        tdef.is_aux = entry["is_aux"]
        if "binning" in entry:
            tdef.bin_type = BinType.VARIABLE
            tdef.binning = array("d", entry["binning"])
        else:
            tdef.bin_type = BinType.FIXED
            tdef.nbins = entry.get("nbins")
            tdef.xmin = entry.get("xmin")
            tdef.xmax = entry.get("xmax")
        if "ALL" in tdef.regions:
            tdef.regions = all_regions
        template_defs.append(tdef)

    radhilo_template_defs = []
    fsr2005_template_defs = []
    for entry in template_defs:
        tdef_isrhi, tdef_isrlo = deepcopy(entry), deepcopy(entry)
        tdef_fsr20, tdef_fsr05 = deepcopy(entry), deepcopy(entry)
        tdef_isrhi.weight, tdef_isrlo.weight = "weight_sys_radHi", "weight_sys_radLo"
        tdef_isrhi.weight_suffix, tdef_isrlo.weight_suffix = "radHi", "radLo"
        tdef_fsr20.weight, tdef_fsr05.weight = "weight_sys_fsr20", "weight_sys_fsr05"
        tdef_fsr20.weight_suffix, tdef_fsr05.weight_suffix = "fsr20", "fsr05"
        if "radHi" not in args.exclude_weights:
            radhilo_template_defs.append(tdef_isrhi)
        if "radLo" not in args.exclude_weights:
            radhilo_template_defs.append(tdef_isrlo)
        if "fsr20" not in args.exclude_weights:
            fsr2005_template_defs.append(tdef_fsr20)
        if "fsr05" not in args.exclude_weights:
            fsr2005_template_defs.append(tdef_fsr05)

    if args.noweightsys:
        return template_defs + radhilo_template_defs + fsr2005_template_defs

    wsys_template_defs = []
    for entry in template_defs:
        for title, sysweight in six.iteritems(SYS_WEIGHTS):
            if sysweight.tiny and not args.do_tiny:
                log.debug("Skipping because tiny: {} {}".format(title, sysweight))
                continue
            if title in args.exclude_weights:
                log.debug("Skipping because excluded: {} {}".format(title, sysweight))
                continue
            tdef_up, tdef_dn = deepcopy(entry), deepcopy(entry)
            tdef_up.weight, tdef_dn.weight = sysweight.branch_up, sysweight.branch_down
            tdef_up.weight_suffix = "{}_{}".format(title, "Up")
            tdef_dn.weight_suffix = "{}_{}".format(title, "Down")
            wsys_template_defs.append(tdef_up)
            wsys_template_defs.append(tdef_dn)

    pdf_template_defs = []
    for entry in template_defs:
        for title, pdfweight in six.iteritems(PDF_WEIGHTS):
            if pdfweight.tiny and not args.do_tiny:
                log.debug("Skipping because tiny: {} {}".format(title, sysweight))
                continue
            if title in args.exclude_weights:
                log.debug("Skipping because excluded: {} {}".format(title, sysweight))
                continue
            tdef_pdf = deepcopy(entry)
            tdef_pdf.weight = pdfweight.branch
            tdef_pdf.weight_suffix = title
            pdf_template_defs.append(tdef_pdf)

    return (
        template_defs
        + radhilo_template_defs
        + fsr2005_template_defs
        + wsys_template_defs
        + pdf_template_defs
    )


def ntuple_definitions(nominal_files, systematic_files, root_dir):
    ntuple_defs = []
    for key, value in six.iteritems(nominal_files):
        sdef = NtupleDefinition()
        sdef.name = key
        sdef.files = ["{}/{}".format(root_dir, f) for f in value]
        if key == "Data":
            sdef.ntype = NtupleType.DATA
        else:
            sdef.ntype = NtupleType.NOMINAL
        ntuple_defs.append(sdef)
    for key, value in six.iteritems(systematic_files):
        sdef = NtupleDefinition()
        sdef.name = key[0]
        sdef.files = ["{}/{}".format(root_dir, f) for f in value]
        sdef.ntype = NtupleType.SYSTEMATIC
        sdef.tree_systematic = key[1]
        ntuple_defs.append(sdef)
    return ntuple_defs


CPP_SHIFT_CODE = """
void shiftScaleSetDir(TH1* h, TFile* file) {
  if (h == nullptr) {
    return;
  }
  int nb = h->GetNbinsX();

  h->AddBinContent(1, h->GetBinContent(0));
  h->SetBinError(1, TMath::Sqrt(TMath::Power(h->GetBinError(0), 2) +
                                TMath::Power(h->GetBinError(1), 2)));

  h->AddBinContent(nb, h->GetBinContent(nb + 1));
  h->SetBinError(nb, TMath::Sqrt(TMath::Power(h->GetBinError(nb), 2) +
                                 TMath::Power(h->GetBinError(nb + 1), 2)));

  h->SetBinContent(0, 0.0);
  h->SetBinError(0, 0.0);
  h->SetBinContent(nb + 1, 0.0);
  h->SetBinError(nb + 1, 0.0);

  auto dir = gDirectory;
  file->cd();
  h->Write("", TObject::kOverwrite);
  h->SetDirectory(0);
  dir->cd();
}
"""


def rdf_runner(args):
    if IN_ATLAS_RELEASE:
        log.info("Operating in ATLAS release")
    else:
        log.info("Operating standalone")
    if args.debug:
        log.setLevel(logging.DEBUG)
    if not args.disable_imt:
        ROOT.ROOT.EnableImplicitMT()
    file_list = os.listdir(args.directory)
    if args.config == "auto":
        confname = "../WtAna/WtStat/data/config.yml"
    else:
        confname = args.config
    with open(confname, "r") as f:
        if IN_ATLAS_RELEASE:
            config = yaml.load(f)
        else:
            config = yaml.load(f, Loader=yaml.FullLoader)

    nominal_sorted_files = sortfiles_nominal(file_list)
    if args.notreesys:
        systematic_sorted_files = {}
    else:
        systematic_sorted_files = sortfiles_systematic(file_list, args)
    regions = region_definitions(config)
    templates = template_definitions(config, args)
    ntuples = ntuple_definitions(nominal_sorted_files, systematic_sorted_files, args.directory)

    out_file = ROOT.TFile.Open(args.outfile, "UPDATE")
    file_keys = [str(k.GetName()) for k in out_file.GetListOfKeys()]
    started_empty = len(file_keys) < 5

    ROOT.gInterpreter.ProcessLine(CPP_SHIFT_CODE)

    nntuples = len(ntuples)
    for i, ntuple in enumerate(ntuples):
        ntuple_is_ttbar_or_tW = ntuple.name == "tW" or ntuple.name == "ttbar"
        chain = ROOT.TChain("{}_{}".format(args.tree_prefix, ntuple.tree_name))
        tree_suffix = ""
        if ntuple.ntype == NtupleType.SYSTEMATIC:
            tree_suffix = "_{}".format(ntuple.tree_name)
        for fname in ntuple.files:
            chain.Add(fname)
        df = RDataFrame(chain)
        df_histograms = []
        # fmt: off
        for region in regions:
            filt = df.Filter(region.selection)
            for template in templates:
                if template.is_aux and not args.do_aux:
                    continue
                if region.name not in template.regions:
                    continue
                weight_suffix = ""
                if ("radLo" in template.weight or
                    "radHi" in template.weight or
                    "fsr20" in template.weight or
                    "fsr05" in template.weight):
                    if  ntuple.ntype == NtupleType.SYSTEMATIC:
                        continue
                    if ntuple.name not in ["ttbar_RU_AFII", "ttbar_AFII", "ttbar", "tW"]:
                        continue
                    weight_suffix = "_{}".format(template.weight_suffix)
                elif template.weight != "weight_nominal":
                    if  ntuple.ntype == NtupleType.SYSTEMATIC:
                        continue
                    if not ntuple_is_ttbar_or_tW:
                        continue
                    weight_suffix = "_{}".format(template.weight_suffix)
                hist_name = "{rname}_{vname}_{sname}{tree_suffix}{weight_suffix}".format(
                    rname=region.name, vname=template.var, sname=ntuple.name,
                    tree_suffix=tree_suffix, weight_suffix=weight_suffix)
                log.debug("Working on {}".format(hist_name))
                if out_file.GetListOfKeys().Contains(hist_name):
                    log.debug("Skipping {} already in file".format(hist_name))
                    continue
                bin_instructor = template
                if template.use_region_binning:
                    bin_instructor = region
                if bin_instructor.bin_type == BinType.VARIABLE:
                    hmodel = TH1DModel(hist_name, ";{};".format(template.axis_title),
                                       len(bin_instructor.binning) - 1, bin_instructor.binning)
                elif bin_instructor.bin_type == BinType.FIXED:
                    hmodel = TH1DModel(hist_name, ";{};".format(template.axis_title),
                                       bin_instructor.nbins, bin_instructor.xmin, bin_instructor.xmax)
                else:
                    log.error("something is wrong {} {}".format(bin_instructor.bin_type, bin_instructor.name))
                df_histograms.append(filt.Histo1D(hmodel, template.var, template.weight))

            if args.force_graph:
                SaveGraph(filt, "test.dot")
        # fmt: on

        for dfh in df_histograms:
            if dfh:
                ROOT.shiftScaleSetDir(dfh.GetPtr(), out_file)
        log.info(
            "Done with <sample: {}, tree: {}> (frame {}/{})".format(
                ntuple.name, ntuple.tree_name, i + 1, nntuples
            )
        )

    out_file.Close()
    return 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="WtStat executions")
    rdf_args(parser)
    args = parser.parse_args()
    rdf_runner(args)
