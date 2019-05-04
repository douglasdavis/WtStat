from __future__ import print_function

import os
import re
import yaml

import WtStat.systematics
from WtStat.ntuple_utils import files_from_dir


def block(block_type, block_title, **options):
    ret = '{}: "{}"'.format(block_type, block_title)
    for k, v in options.items():
        ret = "{}\n  {}: {}".format(ret, k, v)
    return "{}\n\n".format(ret)


def Job(name, npath, lumi):
    bk = block(
        "Job",
        name,
        CmeLabel='"13 TeV"',
        POI='"SigXsecOverSM"',
        ReadFrom="NTUP",
        Lumi=lumi,
        LumiLabel='"{} fb^{{-1}}"'.format(lumi),
        NtuplePath=npath,
        NtupleName="WtTMVA_nominal",
        # MCweight='"weight_nominal"',
        DebugLevel=1,
        MCstatThreshold=0.005,
        SystControlPlots="TRUE",
        SystPruningShape=0.005,
        SystPruningNorm=0.005,
        ImageFormat='"pdf"',
        SystCategoryTables="TRUE",
        RankingPlot="Systs",
        RankingMaxNP=15,
        DoSummaryPlot="TRUE",
        DoTables="TRUE",
        TableOptions="STANDALONE",
        CorrelationThreshold=0.35,
        DoSignalRegionsPlot="TRUE",
        DoPieChartPlot="TRUE",
        PlotOptions="NOXERR",
        UseATLASRoundingTxt="TRUE",
        UseATLASRoundingTex="TRUE",
        HistoChecks="NOCRASH",
        LegendNColumns=1,
        SplitHistoFiles="TRUE",
    )
    return bk


def Fit(name, blind="TRUE", NumCPU=6):
    bk = block(
        "Fit",
        name,
        FitType="SPLUSB",
        FitRegion="CRSR",
        NumCPU=NumCPU,
        POIAsimov=1,
        FitBlind=blind,
        # UseMinos='"ttbar_HS"',
    )
    return bk


def Region_1j1b():
    bk = r"""
Region: reg1j1b
  Type: SIGNAL
  Selection: "reg1j1b==1&&elmu==1&&OS==1"
  Variable: "bdt_response",25,-0.6,0.7
  VariableTitle: "BDT"
  Label: 1j1b
  ShortLabel: 1j1b
  %Binning: "AutoBin","TransfoD",5,15
"""
    return bk


def Region_2j1b():
    bk = r"""
Region: reg2j1b
  Type: SIGNAL
  Selection: "reg2j1b==1&&elmu==1&&OS==1"
  Variable: "bdt_response",25,-0.6,0.7
  VariableTitle: "BDT"
  Label: 2j1b
  ShortLabel: 2j1b
  %Binning: "AutoBin","TransfoD",5,15
"""
    return bk


def Region_2j2b():
    bk = r"""
Region: reg2j2b
  Type: SIGNAL
  Selection: "reg2j2b==1&&elmu==1&&OS==1"
  Variable: "bdt_response",25,-0.7,0.95
  VariableTitle: "BDT"
  Label: 2j2b
  ShortLabel: 2j2b
  %Binning: "AutoBin","TransfoD",5,15
"""
    return bk


def Region_3j():
    bk = r"""
Region: reg3j
  Type: SIGNAL
  Selection: "reg3j==1&&elmu==1&&OS==1"
  Variable: "bdt_response",25,-0.7,0.7
  VariableTitle: "BDT"
  Label: 3j
  ShortLabel: 3j
  %Binning: "AutoBin","TransfoD",5,15
"""
    return bk


def Region_3jpT():
    bk = r"""
Region: reg3j
  Type: SIGNAL
  Selection: "reg3j==1&&elmu==1&&OS==1"
  Variable: "pT_jet2",25,25,175
  VariableTitle: "#it{p}_{T}(jet2) [GeV]"
  Label: 3j
  ShortLabel: 3j
"""
    return bk


def Region_3j1b():
    bk = r"""
Region: reg3j1b
  Type: SIGNAL
  Selection: "reg3j1b==1&&elmu==1&&OS==1"
  Variable: "bdt_response",25,-0.8,0.6
  VariableTitle: "BDT"
  Label: 3j1b
  ShortLabel: 3j1b
  %Binning: "AutoBin","TransfoD",5,15
"""
    return bk


def Sample_tWghost(ntupdir):
    files = files_from_dir(ntupdir, r"^tW_DR_41064(8|9)_AFII_MC16(a|d|e).root$")
    bk = r"""
Sample: tWghost
  Type: GHOST
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_tWpdfghost(ntupdir):
    files = files_from_dir(ntupdir, r"^tW_DR_41064(8|9)_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: tWpdfghost
  Type: GHOST
  MCweight: "weight_sys_PDFset=90900"
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_ttbarghost(ntupdir):
    files = files_from_dir(ntupdir, r"^ttbar_410472_AFII_MC16(a|d|e).root$")
    bk = r"""
Sample: ttbarghost
  Type: GHOST
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_ttbarpdfghost(ntupdir):
    files = files_from_dir(ntupdir, r"^ttbar_410472_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: ttbarpdfghost
  Type: GHOST
  MCweight: "weight_sys_PDFset=90900"
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_Data(ntupdir):
    files = files_from_dir(ntupdir, r"^Data[0-9]{2}(\w|\W)+root$")
    bk = r"""
Sample: Data
  Type: DATA
  Title: "Data"
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_tW(ntupdir):
    files = files_from_dir(ntupdir, r"^tW_DR_41064(8|9)_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: tW
  Type: SIGNAL
  Title: "#it{{tW}}"
  TexTitle: "$tW$"
  FillColor: 861
  LineColor: 1
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_ttbar(ntupdir):
    files = files_from_dir(ntupdir, r"^ttbar_410472_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: ttbar
  Type: BACKGROUND
  Title: "#it{{t#bar{{t}}}}"
  TexTitle: "$t\bar{{t}}$"
  FillColor: 633
  LineColor: 1
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_Diboson(ntupdir):
    files = files_from_dir(ntupdir, r"^Diboson_[0-9]{6}_FS_MC16(a|d|e)(\w|\W)+root$")
    bk = r"""
Sample: Diboson
  Type: BACKGROUND
  Title: "Diboson"
  TexTitle: "Diboson"
  FillColor: 400
  LineColor: 1
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_Zjets(ntupdir):
    files = files_from_dir(ntupdir, r"^Zjets_[0-9]{6}_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: Zjets
  Type: BACKGROUND
  Title: "#it{{Z}}+jets"
  TexTitle: "$Z+$jets"
  FillColor: 801
  LineColor: 1
  MCweight: weight_nominal
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def Sample_MCNP(ntupdir):
    files = files_from_dir(ntupdir, r"^MCNP_\w+_[0-9]{6}_FS_MC16(a|d|e).root$")
    bk = r"""
Sample: MCNP
  Type: BACKGROUND
  Title: "MCNP"
  TexTitle: "MCNP"
  FillColor: 615
  MCweight: weight_nominal
  LineColor: 1
  NtupleFiles: {}
""".format(
        files
    )
    return bk


def NF_tW():
    bk = """
NormFactor: SigXsecOverSM
  Title: "#it{#mu}_{#it{tW}}"
  Nominal: 1
  Min: -100
  Max: 100
  Samples: tW
"""
    return bk


def NF_ttbar():
    bk = """
NormFactor: "mu_tt"
  Title: "#it{#mu}_{#it{t#bar{t}}}"
  Nominal: 1
  Min: 0
  Max: 3
  Samples: ttbar
"""
    return bk


def NF_minor(regions=["1j1b", "2j1b", "2j2b", "3j1b"]):
    ret = []
    if "1j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_Diboson_1j1b
  Title: "Norm Diboson 1j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Diboson
  Category: Norms
  Regions: reg1j1b"""
        )

    if "2j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_Diboson_2j1b
  Title: "Norm Diboson 2j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Diboson
  Category: Norms
  Regions: reg2j1b"""
        )

    if "2j2b" in regions:
        ret.append(
            r"""
Systematic: Norm_Diboson_2j2b
  Title: "Norm Diboson 2j2b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Diboson
  Category: Norms
  Regions: reg2j2b"""
        )

    if "3j" in regions:
        ret.append(
            """
Systematic: Norm_Diboson_3j
  Title: "Norm Diboson 3j"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Diboson
  Category: Norms
  Regions: reg3j"""
        )

    if "3j1b" in regions:
        ret.append(
            """
Systematic: Norm_Diboson_3j1b
  Title: "Norm Diboson 3j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Diboson
  Category: Norms
  Regions: reg3j1b"""
        )

    if "1j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_Zjets_1j1b
  Title: "Norm Zjets 1j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Zjets
  Category: Norms
  Regions: reg1j1b"""
        )

    if "2j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_Zjets_2j1b
  Title: "Norm Zjets 2j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Zjets
  Category: Norms
  Regions: reg2j1b"""
        )

    if "2j2b" in regions:
        ret.append(
            r"""
Systematic: Norm_Zjets_2j2b
  Title: "Norm Zjets 2j2b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Zjets
  Category: Norms
  Regions: reg2j2b"""
        )

    if "3j" in regions:
        ret.append(
            r"""
Systematic: Norm_Zjets_3j
  Title: "Norm Zjets 3j"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Zjets
  Category: Norms
  Regions: reg3j"""
        )

    if "3j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_Zjets_3j1b
  Title: "Norm Zjets 3j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: Zjets
  Category: Norms
  Regions: reg3j1b"""
        )

    if "1j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_MCNP_1j1b
  Title: "Norm MCNP 1j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: MCNP
  Category: Norms
  Regions: reg1j1b"""
        )

    if "2j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_MCNP_2j1b
  Title: "Norm MCNP 2j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: MCNP
  Category: Norms
  Regions: reg2j1b"""
        )

    if "2j2b" in regions:
        ret.append(
            r"""
Systematic: Norm_MCNP_2j2b
  Title: "Norm MCNP 2j2b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: MCNP
  Category: Norms
  Regions: reg2j2b"""
        )

    if "3j" in regions:
        ret.append(
            r"""
Systematic: Norm_MCNP_3j
  Title: "Norm MCNP 3j"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: MCNP
  Category: Norms
  Regions: reg3j"""
        )

    if "3j1b" in regions:
        ret.append(
            r"""
Systematic: Norm_MCNP_3j1b
  Title: "Norm MCNP 3j1b"
  Type: OVERALL
  OverallUp: 0.5
  OverallDown: -0.5
  Samples: MCNP
  Category: Norms
  Regions: reg3j1b"""
        )

    return "{}{}".format("\n".join(ret), "\n")


def get_sys_weights(do_smoothing=False):
    sys_weight_blocks = []
    for title, options in WtStat.systematics.SYS_WEIGHTS.items():
        upw = options[0]
        downw = options[1]
        category = options[2]
        smoothing = options[3]
        propertitle = options[4]
        sysblock = block(
            "Systematic",
            title,
            Title='"{}"'.format(propertitle),
            Samples="tW,ttbar",
            WeightUp="{}".format(upw),
            WeightDown="{}".format(downw),
            Symmetrisation="TWOSIDED",
            Category='"{}"'.format(category),
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)
        sys_weight_blocks.append(sysblock)
    return "".join(sys_weight_blocks)


def get_tW_pdf_weights(do_smoothing=False):
    pdf_blocks = []
    for title, options in WtStat.systematics.PDF_WEIGHTS.items():
        if "90900" in title:
            continue
        upw = options[0]
        category = options[1]
        smoothing = options[2]
        sysblock = block(
            "Systematic",
            "{}_tW".format(title),
            Title='"{}_tW"'.format(title),
            Samples="tW",
            WeightUp="weight_sys_{}".format(title.replace("set","set=")),
            NuisanceParameter='"{}"'.format(title),
            Category="PDFs",
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)

        pdf_blocks.append(sysblock)
    return "".join(pdf_blocks)


def get_ttbar_pdf_weights(do_smoothing=False):
    pdf_blocks = []
    for title, options in WtStat.systematics.PDF_WEIGHTS.items():
        if "90900" in title:
            continue
        upw = options[0]
        category = options[1]
        smoothing = options[2]
        sysblock = block(
            "Systematic",
            "{}_ttbar".format(title),
            Title='"{}_ttbar"'.format(title),
            Samples="ttbar",
            WeightUp="weight_sys_{}".format(title.replace("set","set=")),
            NuisanceParameter='"{}"'.format(title),
            Category="PDFs",
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)

        pdf_blocks.append(sysblock)
    return "".join(pdf_blocks)


def get_sys_trees2s(do_smoothing=False):
    sys_tree_blocks = []
    for title, options in WtStat.systematics.SYS_TREES_TWOSIDED.items():
        upt = options[0]
        downt = options[1]
        category = options[2]
        smoothing = options[3]
        sysblock = block(
            "Systematic",
            title,
            Title='"{}"'.format(title.replace("_", "")),
            Samples="tW,ttbar",
            NtupleFileSufUp="_{}.bdt_response".format(upt),
            NtupleFileSufDown="_{}.bdt_response".format(downt),
            NtupleNameUp="WtTMVA_{}".format(upt),
            NtupleNameDown="WtTMVA_{}".format(downt),
            Symmetrisation="TWOSIDED",
            Category='"{}"'.format(category),
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)
        sys_tree_blocks.append(sysblock)
    return "".join(sys_tree_blocks)


def get_sys_trees1s(do_smoothing=False):
    sys_tree_blocks = []
    for title, options in WtStat.systematics.SYS_TREES_ONESIDED.items():
        upt = options[0]
        category = options[1]
        smoothing = options[2]
        sysblock = block(
            "Systematic",
            title,
            Title='"{}"'.format(title.replace("_", "")),
            Samples="tW,ttbar",
            NtupleFileSufUp="_{}.bdt_response".format(upt),
            NtupleNameUp="WtTMVA_{}".format(upt),
            Symmetrisation="ONESIDED",
            Category='"{}"'.format(category),
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)
        sys_tree_blocks.append(sysblock)
    return "".join(sys_tree_blocks)
