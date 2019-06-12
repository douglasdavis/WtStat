#!/usr/bin/env python

import os
import re
import math
from copy import deepcopy
from array import array
from collections import OrderedDict
import yaml
from WtStat.enum import Enum
from WtStat.systematics import SYS_WEIGHTS, PDF_WEIGHTS

import logging

log = logging.getLogger(__name__)

# fmt: off
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
RDataFrame = ROOT.ROOT.RDataFrame
TH1DModel = ROOT.ROOT.RDF.TH1DModel
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

    # fmt: off
    def __repr__(self):

        return "<TemplateDefinition: {}>".format(
            ", ".join([self.var, self.weight, str(self.weight_suffix), str(self.regions),
                       str(self.use_region_binning), str(self.binning), str(self.nbins),
                       str(self.xmin), str(self.xmax), self.axis_title]))
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
            for k, v in NOMINAL_REGEXES.items():
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

    if args.noweightsys:
        return template_defs

    wsys_template_defs = []
    for entry in template_defs:
        for key, value in SYS_WEIGHTS.iteritems():
            if key in args.exclude_weights:
                continue
            tdef_up, tdef_dn = deepcopy(entry), deepcopy(entry)
            tdef_up.weight, tdef_dn.weight = value[0], value[1]
            tdef_up.weight_suffix = "{}_{}".format(key, "Up")
            tdef_dn.weight_suffix = "{}_{}".format(key, "Down")
            wsys_template_defs.append(tdef_up)
            wsys_template_defs.append(tdef_dn)

    radhilo_template_defs = []
    for entry in template_defs:
        tdef_hi, tdef_lo = deepcopy(entry), deepcopy(entry)
        tdef_hi.weight, tdef_lo.weight = "weight_sys_radHi", "weight_sys_radLo"
        tdef_hi.weight_suffix, tdef_lo.weight_suffix = "radHi", "radLo"
        if "radHi" not in args.exclude_weights:
            radhilo_template_defs.append(tdef_hi)
        if "radLo" not in args.exclude_weights:
            radhilo_template_defs.append(tdef_lo)

    pdf_template_defs = []
    for entry in template_defs:
        for key, value in PDF_WEIGHTS.iteritems():
            if key in args.exclude_weights:
                continue
            tdef_pdf = deepcopy(entry)
            tdef_pdf.weight = value[0]
            tdef_pdf.weight_suffix = key
            pdf_template_defs.append(tdef_pdf)

    return template_defs + wsys_template_defs + radhilo_template_defs + pdf_template_defs


def ntuple_definitions(nominal_files, systematic_files, root_dir):
    ntuple_defs = []
    for key, value in nominal_files.iteritems():
        sdef = NtupleDefinition()
        sdef.name = key
        sdef.files = ["{}/{}".format(root_dir, f) for f in value]
        if key == "Data":
            sdef.ntype = NtupleType.DATA
        else:
            sdef.ntype = NtupleType.NOMINAL
        ntuple_defs.append(sdef)
    for key, value in systematic_files.iteritems():
        sdef = NtupleDefinition()
        sdef.name = key[0]
        sdef.files = ["{}/{}".format(root_dir, f) for f in value]
        sdef.ntype = NtupleType.SYSTEMATIC
        sdef.tree_systematic = key[1]
        ntuple_defs.append(sdef)
    return ntuple_defs


CPP_SHIFT_CODE = """
void shiftScaleSetDir(TH1D* h, float lumi, TFile* file) {
  int nb = h->GetNbinsX();

  double v_under = h->GetBinContent(0);
  double v_over = h->GetBinContent(nb + 1);

  double e_under = h->GetBinError(0);
  double e_over = h->GetBinError(nb + 1);

  double v_first = h->GetBinContent(1);
  double v_last = h->GetBinContent(nb);

  double e_first = h->GetBinError(1);
  double e_last = h->GetBinError(nb);

  h->SetBinContent(1, v_under + v_first);
  h->SetBinContent(nb, v_over + v_last);
  h->SetBinError(1, std::sqrt(e_under * e_under + e_first * e_first));
  h->SetBinError(nb, std::sqrt(e_over * e_over + e_last * e_last));

  h->SetBinContent(0, 0.0);
  h->SetBinContent(nb + 1, 0, 0);
  h->SetBinError(0, 0.0);
  h->SetBinError(nb + 1, 0.0);

  h->SetDirectory(file);
  h->Write();
}
"""


def rdf_runner(args):
    if args.debug:
        log.setLevel(logging.DEBUG)
    if not args.disable_imt:
        ROOT.ROOT.EnableImplicitMT()
    file_list = os.listdir(args.directory)
    with open(args.config, "r") as f:
        config = yaml.load(f)

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
                if region.name not in template.regions:
                    continue
                weight_suffix = ""
                if "radLo" in template.weight or "radHi" in template.weight:
                    if  ntuple.ntype == NtupleType.SYSTEMATIC:
                        continue
                    if ntuple.name not in ["ttbar_RU_AFII", "ttbar_AFII", "tW"]:
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
                if hist_name in file_keys:
                    log.warn("Skipping {} already in file".format(hist_name))
                    continue
                if template.use_region_binning:
                    if region.bin_type == BinType.VARIABLE:
                        hmodel = TH1DModel(hist_name, ";{};".format(
                            template.axis_title), len(region.binning) - 1, region.binning)
                    elif region.bin_type == BinType.FIXED:
                        hmodel = TH1DModel(hist_name, ";{};".format(
                            template.axis_title), region.nbins, region.xmin, region.xmax)
                    else:
                        log.error("something is wrong {} {}".format(region.bin_type, region.name))
                else:
                    if template.bin_type == BinType.VARIABLE:
                        hmodel = TH1DModel(hist_name, ";{};".format(
                            template.axis_title), len(template.binning) - 1, template.binning)
                    elif template.bin_type == BinType.FIXED:
                        hmodel = TH1DModel(hist_name, ";{};".format(
                            template.axis_title), template.nbins, template.xmin, template.xmax)
                    else:
                        log.error("something is wrong {} {}".format(template.bin_type, template.var))

                df_histograms.append(filt.Histo1D(hmodel, template.var, template.weight))
        # fmt: on

        for dfh in df_histograms:
            ROOT.shiftScaleSetDir(dfh.GetPtr(), 140.5, out_file)
        log.info(
            "Done with ntuple {} ({}) ({}/{})".format(
                ntuple.name, ntuple.tree_name, i + 1, nntuples
            )
        )

    out_file.Close()
    return 0
