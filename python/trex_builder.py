import os
import yaml
import WtStat.systematics as systematics

import logging
log = logging.getLogger(__name__)

def block(block_type, block_title, **options):
    ret = '{}: "{}"'.format(block_type, block_title)
    for k, v in options.items():
        ret = "{}\n  {}: {}".format(ret, k, v)
    return "{}\n".format(ret)


def Job(args):
    hpath = args.hfile
    histopath = "/".join(os.path.abspath(hpath).split("/")[:-1])
    histofile = os.path.abspath(hpath).split("/")[-1].split(".root")[0]

    JOB = """Job: "{jobname}"
  ReadFrom: HIST
  DebugLevel: 1
  POI: "SigXsecOverSM"
  PlotOptions: NOXERR
  MCstatThreshold: {mcstat}
  SystPruningNorm: {prunenorm}
  SystPruningShape: {pruneshape}
  HistoPath: "{histopath}"
  HistoFile: "{histofile}"
  HistoChecks: NOCRASH
  DoPieChartPlot: TRUE
  CmeLabel: "13 TeV"
  DoSummaryPlot: {dosummaryplot}
  SummaryPlotRegions: reg1j1b,reg2j1b,reg2j2b,reg3j
  DoTables: {dotables}
  SystCategoryTables: {dotables}
  SystControlPlots: {dosysplots}
  SystDataPlots: {dosysplots}
  LegendNColumns: 1
  ImageFormat: "{imgf}"
  Lumi: {lumi}
  LumiLabel: "{lumilab} fb^{{-1}}"
  UseATLASRoundingTxt: TRUE
  UseATLASRoundingTex: TRUE
  TableOptions: STANDALONE
  RankingPlot: Systs
  RankingMaxNP: 20
  RatioYmin: 0.80
  RatioYmax: 1.20
  RatioYminPostFit: 0.90
  RatioYmaxPostFit: 1.10
  SplitHistoFiles: TRUE
  CorrelationThreshold: {cmthresh}
"""
    return JOB.format(jobname=args.job_name,
                      mcstat=args.pruning[0],
                      prunenorm=args.pruning[1],
                      pruneshape=args.pruning[2],
                      histopath=histopath,
                      histofile=histofile,
                      dosummaryplot="FALSE" if args.no_summaryplot else "TRUE",
                      dotables="FALSE" if args.no_tables else "TRUE",
                      dosysplots="FALSE" if args.no_sysplots else "TRUE",
                      lumi=args.lumi,
                      lumilab=round(args.lumi),
                      imgf=args.img_format,
                      cmthresh=args.cm_thresh)


def Fit(args):
    FIT = """
Fit: "{fitname}"
  NumCPU: {ncpu}
  POIAsimov: 1
  FitType: SPLUSB
  FitRegion: CRSR
  FitBlind: TRUE
  UseMinos: all
"""

    return FIT.format(fitname=args.fit_name,
                      ncpu=args.num_cpu)


def Regions(args):
    REGIONS="""
Region: "reg1j1b"
  VariableTitle: "Classifier Response"
  ShortLabel: 1j1b
  HistoName: "reg1j1b{reg_suff}_bdt_response"
  Type: SIGNAL
  Label: 1j1b

Region: "reg2j1b"
  VariableTitle: "Classifier Response"
  ShortLabel: 2j1b
  HistoName: "reg2j1b{reg_suff}_bdt_response"
  Type: SIGNAL
  Label: 2j1b

Region: "reg2j2b"
  VariableTitle: "Classifier Response"
  ShortLabel: 2j2b
  HistoName: "reg2j2b{reg_suff}_bdt_response"
  Type: SIGNAL
  Label: 2j2b

Region: "reg3j"
  ShortLabel: 3j
  VariableTitle: "Classifier Response"
  Type: SIGNAL
  HistoName: "reg3j{reg_suff}_bdt_response_3j"
  Label: 3j
""".format(reg_suff=args.reg_suff)

    vrblocks = []
    if args.vr_plots:
        with open(args.config, "r") as f:
            yam = yaml.load(f)
            for tentry in yam["templates"]:
                if "bdt_response" in tentry["var"]:
                    continue
                for r in tentry["regions"]:
                    btitle = "VR{}_{}".format(r, tentry["var"])
                    hname = '"{}_{}"'.format(r, tentry["var"])
                    label = '"{}"'.format(r.split("reg")[-1])
                    vtitle = '"{}"'.format(tentry["axis_title"])
                    bk = block("Region", btitle,
                               VariableTitle=vtitle, Label=label,
                               Type="VALIDATION", HistoName=hname)
                    REGIONS = "{}\n{}".format(REGIONS, bk)

    return REGIONS


def Samples(args):
    SAMPLES = """
Sample: "tWghost"
  Type: GHOST
  HistoNameSuff: "_tW_AFII"

Sample: "ttbarghost"
  Type: GHOST
  HistoNameSuff: "_ttbar_AFII"

Sample: "Data"
  HistoNameSuff: "_Data"
  Type: DATA
  Title: "Data"

Sample: "tW"
  HistoNameSuff: "_tW"
  Title: "#it{tW}"
  TexTitle: "$tW$"
  FillColor: 862
  LineColor: 1
  Type: SIGNAL

Sample: "ttbar"
  HistoNameSuff: "_ttbar"
  Title: "#it{t#bar{t}}"
  TexTitle: "$t\\bar{t}$"
  FillColor: 634
  LineColor: 1
  Type: BACKGROUND

Sample: "Zjets"
  HistoNameSuff: "_Zjets"
  Title: "#it{Z}+jets"
  TexTitle: "$Z+$jets"
  FillColor: 802
  LineColor: 1
  Type: BACKGROUND

Sample: "Diboson"
  HistoNameSuff: "_Diboson"
  Title: "Diboson"
  TexTitle: "Diboson"
  FillColor: 419
  LineColor: 1
  Type: BACKGROUND

%Sample: "ttV"
%  HistoNameSuff: "_ttV"
%  Title: "ttV"
%  TexTitle: "$t\\bar{t}V$"
%  FillColor: 803
%  LineColor: 1
%  Type: BACKGROUND

Sample: "MCNP"
  HistoNameSuff: "_MCNP"
  Title: "MCNP"
  TexTitle: "MCNP"
  FillColor: 875
  LineColor: 1
  Type: BACKGROUND

NormFactor: "SigXsecOverSM"
  Max: 2
  Nominal: 1
  Min: 0
  Samples: tW
  Title: "#it{#mu}_{#it{tW}}"

NormFactor: "mu_ttbar"
  Max: 1.5
  Nominal: 1
  Min: 0.5
  Samples: ttbar
  Title: "#it{#mu}_{#it{t#bar{t}}}"
"""
    return SAMPLES


def Systematics_fixed():
    BLOCKS = """
Systematic: "Lumi"
  OverallDown: -0.017
  Category: Instrumental
  OverallUp: 0.017
  Title: "Lumi"
  Samples: tW,ttbar,Zjets,Diboson,MCNP
  Type: OVERALL

Systematic: "tW_DRDS"
  Category: "Modeling"
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_DS_FS"
  Samples: tW
  Title: "tW DR vs DS"
  Type: HISTO

Systematic: "tW_HS"
  Category: "Modeling"
  Title: "tW Hard Scatter"
  ReferenceSample: tWghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_MCaNLO_AFII"
  Samples: tW
  Type: HISTO

%Systematic: "tW_PS"
%  Category: "Modeling"
%  Title: "tW Parton Shower"
%  ReferenceSample: tWghost
%  Symmetrisation: ONESIDED
%  HistoNameSufUp: "_H7_AFII"
%  Samples: tW
%  Type: HISTO

Systematic: "tW_PS_1j1b"
  Category: "Modeling"
  Title: "tW Parton Shower 1j1b"
  ReferenceSample: tWghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: tW
  Type: HISTO
  Regions: reg1j1b

Systematic: "tW_PS_2j1b"
  Category: "Modeling"
  Title: "tW Parton Shower 2j1b"
  ReferenceSample: tWghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: tW
  Type: HISTO
  Regions: reg2j1b

Systematic: "tW_PS_2j2b"
  Category: "Modeling"
  Title: "tW Parton Shower 2j2b"
  ReferenceSample: tWghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: tW
  Type: HISTO
  Regions: reg2j2b

Systematic: "tW_PS_3j"
  Category: "Modeling"
  Title: "tW Parton Shower 3j"
  ReferenceSample: tWghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: tW
  Type: HISTO
  Regions: reg3j

%Systematic: "tW_AR_ISR"
%  Category: "Modeling"
%  Title: "tW ISR"
%  HistoNameSufUp: "_isrCombRadHi"
%  HistoNameSufDown: "_isrCombRadLo"
%  Symmetrisation: TWOSIDED
%  Samples: tW
%  Type: HISTO


Systematic: "tW_AR_ISR_scale"
  Category: "Modeling"
  Title: "tW ISR Scale Variations"
  HistoNameSufUp: "_20muRF"
  HistoNameSufDown: "_05muRF"
  Symmetrisation: TWOSIDED
  Samples: tW
  Type: HISTO

Systematic: "tW_AR_ISR_A14"
  Category: "Modeling"
  Title: "tW ISR A14"
  HistoNameSufUp: "_Var3cUp"
  HistoNameSufDown: "_Var3cDown"
  Symmetrisation: TWOSIDED
  Samples: tW
  Type: HISTO

Systematic: "tW_AR_FSR"
  Category: "Modeling"
  Title: "tW FSR"
  HistoNameSufDown: "_fsr20"
  HistoNameSufUp: "_fsr05"
  Symmetrisation: TWOSIDED
  Samples: tW
  Type: HISTO

Systematic: "ttbar_HS"
  Category: "Modeling"
  Title: "ttbar Hard Scatter"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_MCaNLO_AFII"
  Samples: ttbar
  Type: HISTO

%Systematic: "ttbar_PS"
%  Category: "Modeling"
%  Title: "ttbar Parton Shower"
%  ReferenceSample: ttbarghost
%  Symmetrisation: ONESIDED
%  HistoNameSufUp: "_H7_AFII"
%  Samples: ttbar
%  Type: HISTO

Systematic: "ttbar_PS_1j1b"
  Category: "Modeling"
  Title: "ttbar Parton Shower 1j1b"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: ttbar
  Type: HISTO
  Regions: reg1j1b

Systematic: "ttbar_PS_2j1b"
  Category: "Modeling"
  Title: "ttbar Parton Shower 2j1b"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: ttbar
  Type: HISTO
  Regions: reg2j1b

Systematic: "ttbar_PS_2j2b"
  Category: "Modeling"
  Title: "ttbar Parton Shower 2j2b"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: ttbar
  Type: HISTO
  Regions: reg2j2b

Systematic: "ttbar_PS_3j"
  Category: "Modeling"
  Title: "ttbar Parton Shower 3j"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  HistoNameSufUp: "_H7_AFII"
  Samples: ttbar
  Type: HISTO
  Regions: reg3j

%Systematic: "ttbar_AR_ISR"
%  Category: "Modeling"
%  Title: "ttbar ISR"
%  HistoNameSufUp: "_RU_AFII_isrCombRadHi"
%  HistoNameSufDown: "_AFII_isrCombRadLo"
%  ReferenceSample: ttbarghost
%  Symmetrisation: TWOSIDED
%  Samples: ttbar
%  Type: HISTO

Systematic: "ttbar_AR_ISR_hdamp"
  Category: "Modeling"
  Title: "ttbar ISR hdamp"
  HistoNameSufUp: "_RU_AFII"
  ReferenceSample: ttbarghost
  Symmetrisation: ONESIDED
  Samples: ttbar
  Type: HISTO

Systematic: "ttbar_AR_ISR_scale"
  Category: "Modeling"
  Title: "ttbar ISR Scale Variations"
  HistoNameSufUp: "_20muRF"
  HistoNameSufDown: "_05muRF"
  Symmetrisation: TWOSIDED
  Samples: ttbar
  Type: HISTO

Systematic: "ttbar_AR_ISR_A14"
  Category: "Modeling"
  Title: "ttbar ISR A14"
  HistoNameSufUp: "_Var3cUp"
  HistoNameSufDown: "_Var3cDown"
  Symmetrisation: TWOSIDED
  Samples: ttbar
  Type: HISTO

Systematic: "ttbar_AR_FSR"
  Category: "Modeling"
  Title: "ttbar FSR"
  HistoNameSufDown: "_fsr20"
  HistoNameSufUp: "_fsr05"
  Symmetrisation: TWOSIDED
  Samples: ttbar
  Type: HISTO

Systematic: "Norm_Diboson_1j1b"
  Type: OVERALL
  Title: "Norm Diboson 1j1b"
  Regions: reg1j1b
  Samples: Diboson
  OverallUp: 0.25
  OverallDown: -0.25
  Category: "Norms"

Systematic: "Norm_Diboson_2j1b"
  Type: OVERALL
  Title: "Norm Diboson 2j1b"
  Regions: reg2j1b
  Samples: Diboson
  OverallUp: 0.25
  OverallDown: -0.25
  Category: "Norms"

Systematic: "Norm_Diboson_2j2b"
  Type: OVERALL
  Title: "Norm Diboson 2j2b"
  Regions: reg2j2b
  Samples: Diboson
  OverallUp: 0.25
  OverallDown: -0.25
  Category: "Norms"

Systematic: "Norm_Diboson_3j"
  Type: OVERALL
  Title: "Norm Diboson 3j"
  Regions: reg3j
  Samples: Diboson
  OverallUp: 0.25
  OverallDown: -0.25
  Category: "Norms"

Systematic: "Norm_Zjets_1j1b"
  Type: OVERALL
  Title: "Norm Zjets 1j1b"
  Regions: reg1j1b
  Samples: Zjets
  OverallUp: 0.20
  OverallDown: -0.20
  Category: "Norms"

Systematic: "Norm_Zjets_2j1b"
  Type: OVERALL
  Title: "Norm Zjets 2j1b"
  Regions: reg2j1b
  Samples: Zjets
  OverallUp: 0.20
  OverallDown: -0.20
  Category: "Norms"

Systematic: "Norm_Zjets_2j2b"
  Type: OVERALL
  Title: "Norm Zjets 2j2b"
  Regions: reg2j2b
  Samples: Zjets
  OverallUp: 0.20
  OverallDown: -0.20
  Category: "Norms"

Systematic: "Norm_Zjets_3j"
  Type: OVERALL
  Title: "Norm Zjets 3j"
  Regions: reg3j
  Samples: Zjets
  OverallUp: 0.20
  OverallDown: -0.20
  Category: "Norms"

Systematic: "Norm_MCNP_1j1b"
  Type: OVERALL
  Title: "Norm MCNP 1j1b"
  Regions: reg1j1b
  Samples: MCNP
  OverallUp: 1.0
  OverallDown: -1.0
  Category: "Norms"

Systematic: "Norm_MCNP_2j1b"
  Type: OVERALL
  Title: "Norm MCNP 2j1b"
  Regions: reg2j1b
  Samples: MCNP
  OverallUp: 1.0
  OverallDown: -1.0
  Category: "Norms"

Systematic: "Norm_MCNP_2j2b"
  Type: OVERALL
  Title: "Norm MCNP 2j2b"
  Regions: reg2j2b
  Samples: MCNP
  OverallUp: 1.0
  OverallDown: -1.0
  Category: "Norms"

Systematic: "Norm_MCNP_3j"
  Type: OVERALL
  Title: "Norm MCNP 3j"
  Regions: reg3j
  Samples: MCNP
  OverallUp: 1.0
  OverallDown: -1.0
  Category: "Norms"

"""
    return BLOCKS


def Systematics_weights(args):
    los = []
    for title, sys_weight in systematics.SYS_WEIGHTS.iteritems():
        if args.skip_tiny and sys_weight.tiny:
            continue
        b = block("Systematic", title,
                  HistoNameSufDown='"_{}_Down"'.format(title),
                  HistoNameSufUp='"_{}_Up"'.format(title),
                  Category='"{}"'.format(sys_weight.category),
                  Title='"{}"'.format(sys_weight.title),
                  Samples="tW,ttbar",
                  Symmetrisation="TWOSIDED",
                  Type="HISTO")
        los.append(b)

    for title, pdf_weight in systematics.PDF_WEIGHTS.iteritems():
        if args.skip_tiny and pdf_weight.tiny:
            continue
        if title == "PDFset90900":
            continue
        b = block("Systematic", title,
                  HistoNameSufUpRefSample='"_PDFset90900"',
                  HistoNameSufUp='"_{}"'.format(title),
                  NuisanceParameter='"{}"'.format(title),
                  Category='"PDFs"',
                  Title='"{}"'.format(pdf_weight.title),
                  Samples="tW,ttbar",
                  Symmetrisation="ONESIDED",
                  Type="HISTO")
        los.append(b)


    return "\n".join(los)


def Systematics_trees(args):
    los = []
    for title, sys_tree in systematics.SYS_TREES_TWOSIDED.iteritems():
        if args.skip_tiny and sys_tree.tiny:
            continue
        b = block("Systematic", title,
                  HistoNameSufDown='"_{}"'.format(sys_tree.branch_down),
                  HistoNameSufUp='"_{}"'.format(sys_tree.branch_up),
                  Category='"{}"'.format(sys_tree.category),
                  Samples="tW,ttbar",
                  Symmetrisation="TWOSIDED",
                  Title='"{}"'.format(sys_tree.title),
                  Type="HISTO")
        los.append(b)

    for title, sys_tree in systematics.SYS_TREES_ONESIDED.iteritems():
        if args.skip_tiny and sys_tree.tiny:
            continue
        b = block("Systematic", title,
                  HistoNameSufUp='"_{}"'.format(sys_tree.branch),
                  Category='"{}"'.format(sys_tree.category),
                  Samples="tW,ttbar",
                  Symmetrisation="ONESIDED",
                  Title='"{}"'.format(sys_tree.title),
                  Type="HISTO")
        los.append(b)

    return "\n".join(los)

def tcgen(args):
    log.info("Always check configuration file. By-hand modifications are expected.")
    job = Job(args)
    fit = Fit(args)
    regions = Regions(args)
    samples = Samples(args)
    systematics_fixed = Systematics_fixed()
    systematics_weights = Systematics_weights(args)
    systematics_trees = Systematics_trees(args)
    config = "{}{}{}{}{}{}\n{}".format(job, fit, regions, samples, systematics_fixed, systematics_weights, systematics_trees)

    if os.path.exists(args.out_file):
        log.warn("overwriting file {}".format(args.out_file))
    with open(args.out_file, "w") as f:
        f.write(config)
    return 0
