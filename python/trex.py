from __future__ import print_function

import WtStat.systematics
import yaml


def block(block_type, block_title, **options):
    ret = '{}: "{}"'.format(block_type, block_title)
    for k, v in options.items():
        ret = "{}\n  {}: {}".format(ret, k, v)
    return "{}\n\n".format(ret)


def Job(name, hpath, hfile, lumi, imgf="pdf"):
    bk = block(
        "Job",
        name,
        CmeLabel='"13 TeV"',
        POI='"SigXsecOverSM"',
        ReadFrom="HIST",
        Lumi=lumi,
        LumiLabel='"{} fb^{{-1}}"'.format(lumi),
        HistoPath=hpath,
        HistoFile=hfile,
        DebugLevel=1,
        MCstatThreshold=0.005,
        SystControlPlots="TRUE",
        SystPruningShape=0.005,
        SystPruningNorm=0.005,
        ImageFormat='"{}"'.format(imgf),
        SystCategoryTables="TRUE",
        SystDataPlots="TRUE",
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
        #UseMinos='"ttbar_HS"',
    )
    return bk


def Region_1j1b_TransfoD(zs=5, zb=5):
    bk = block(
        "Region",
        "reg1j1b",
        Type="SIGNAL",
        Label="1j1b",
        ShortLabel="1j1b",
        HistoName='"reg1j1b_bdt_response"',
        VariableTitle='"Classifier Response"',
        Binning='"AutoBin","TransfoD",{zs},{zb}'.format(zs=zs, zb=zb),
    )
    return bk


def Region_2j1b_TransfoD(zs=5, zb=5):
    bk = block(
        "Region",
        "reg2j1b",
        Type="SIGNAL",
        Label="2j1b",
        ShortLabel="2j1b",
        HistoName='"reg2j1b_bdt_response"',
        VariableTitle='"Classifier Response"',
        Binning='"AutoBin","TransfoD",{zs},{zb}'.format(zs=zs, zb=zb),
    )
    return bk


def Region_2j2b_TransfoD(zs=5, zb=5):
    bk = block(
        "Region",
        "reg2j2b",
        Type="SIGNAL",
        Label="2j2b",
        ShortLabel="2j2b",
        HistoName='"reg2j2b_bdt_response"',
        VariableTitle='"Classifier Response"',
        Binning='"AutoBin","TransfoD",{zs},{zb}'.format(zs=zs, zb=zb),
    )
    return bk


def Region_1j1b(rebin=0):
    bk = block(
        "Region",
        "reg1j1b",
        Type="SIGNAL",
        Label="1j1b",
        ShortLabel="1j1b",
        HistoName='"reg1j1b_bdt_response"',
        VariableTitle='"Classifier Response"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_2j1b(rebin=0):
    bk = block(
        "Region",
        "reg2j1b",
        Type="SIGNAL",
        Label="2j1b",
        ShortLabel="2j1b",
        HistoName='"reg2j1b_bdt_response"',
        VariableTitle='"Classifier Response"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_2j2b(rebin=0):
    bk = block(
        "Region",
        "reg2j2b",
        Type="SIGNAL",
        Label="2j2b",
        ShortLabel="2j2b",
        HistoName='"reg2j2b_bdt_response"',
        VariableTitle='"Classifier Response"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_3j(rebin=0):
    bk = block(
        "Region",
        "reg3j",
        Type="SIGNAL",
        Label="3j",
        ShortLabel="3j",
        VariableTitle='"Classifier Response"',
        HistoName='"reg3j_bdt_response"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_3j_pT_jet2(rebin=0):
    bk = block(
        "Region",
        "reg3j",
        Type="SIGNAL",
        Label="3j",
        ShortLabel="3j",
        VariableTitle='"#it{p}_{T}^{jet2} [GeV]"',
        HistoName='"reg3j_pT_jet2"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_4j_pT_jet2(rebin=0):
    bk = block(
        "Region",
        "reg4j",
        Type="CONTROL",
        Label="4j",
        ShortLabel="4j",
        VariableTitle='"#it{p}_{T}^{jet2} [GeV]"',
        HistoName='"reg4j_pT_jet2"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


def Region_3j1b(rebin=0):
    bk = block(
        "Region",
        "reg3j1b",
        Type="SIGNAL",
        VariableTitle='"#it{p}_{T}^{jet2} [GeV]"',
        Label="3j1b",
        ShortLabel="3j1b",
        HistoName='"reg3j1b_pT_jet2"',
    )
    if rebin > 0:
        bk = "{}\n  Rebin: {}\n\n".format(bk.strip(), rebin)
    return bk


tWghost = block("Sample", "tWghost", Type="GHOST", HistoNameSuff='"_tW_AFII"')
ttbarghost = block("Sample", "ttbarghost", Type="GHOST", HistoNameSuff='"_ttbar_AFII"')

ghost_samples = "{}{}".format(tWghost, ttbarghost)

data_sample = block(
    "Sample", "Data", Type="DATA", Title='"Data"', HistoNameSuff='"_Data"'
)

tW_sample = block(
    "Sample",
    "tW",
    Title='"#it{tW}"',
    TexTitle='"$tW$"',
    FillColor=861,
    LineColor=1,
    Type="SIGNAL",
    HistoNameSuff='"_tW"',
)

ttbar_sample = block(
    "Sample",
    "ttbar",
    Title='"#it{t#bar{t}}"',
    TexTitle=r'"$t\bar{t}$"',
    FillColor=633,
    LineColor=1,
    Type="BACKGROUND",
    HistoNameSuff='"_ttbar"',
)

Zjets_sample = block(
    "Sample",
    "Zjets",
    Title='"#it{Z}+jets"',
    TexTitle="$Z+$jets",
    Type="BACKGROUND",
    HistoNameSuff='"_Zjets"',
    FillColor=801,
    LineColor=1,
)

Diboson_sample = block(
    "Sample",
    "Diboson",
    Title='"Diboson"',
    TexTitle='"Diboson"',
    FillColor=400,
    LineColor=1,
    Type="BACKGROUND",
    HistoNameSuff='"_Diboson"',
)

MCNP_sample = block(
    "Sample",
    "MCNP",
    Title='"MCNP"',
    TexTitle='"MCNP"',
    FillColor=615,
    LineColor=1,
    Type="BACKGROUND",
    HistoNameSuff='"_MCNP"',
)

all_samples = [
    ghost_samples,
    data_sample,
    tW_sample,
    ttbar_sample,
    Zjets_sample,
    Diboson_sample,
    MCNP_sample,
]

tW_NF = block(
    "NormFactor",
    "SigXsecOverSM",
    Title='"#it{#mu}_{#it{tW}}"',
    Nominal=1,
    Min=0,
    Max=2,
    Samples="tW",
)


ttbar_NF = block(
    "NormFactor",
    "mu_ttbar",
    Title='"#it{#mu}_{#it{t#bar{t}}}"',
    Nominal=1,
    Min=0.5,
    Max=1.5,
    Samples="ttbar",
)

sys_lumi = block(
    "Systematic",
    "Lumi",
    Type="OVERALL",
    Title='"Lumi"',
    OverallUp=0.02,
    OverallDown=-0.02,
    Samples="all",
    Category="Instrumental",
)

sys_zjets_norm_1j1b = block(
    "Systematic",
    "Norm_Zjets_1j1b",
    Type="OVERALL",
    Title='"Norm Zjets 1j1b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Zjets",
    Regions="reg1j1b",
    Category='"Norms"',
)

sys_zjets_norm_2j1b = block(
    "Systematic",
    "Norm_Zjets_2j1b",
    Type="OVERALL",
    Title='"Norm Zjets 2j1b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Zjets",
    Regions="reg2j1b",
    Category='"Norms"',
)

sys_zjets_norm_2j2b = block(
    "Systematic",
    "Norm_Zjets_2j2b",
    Type="OVERALL",
    Title='"Norm Zjets 2j2b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Zjets",
    Regions="reg2j2b",
    Category='"Norms"',
)

sys_zjets_norm_3j = block(
    "Systematic",
    "Norm_Zjets_3j",
    Type="OVERALL",
    Title='"Norm Zjets 3j"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Zjets",
    Regions="reg3j",
    Category='"Norms"',
)

sys_diboson_norm_1j1b = block(
    "Systematic",
    "Norm_Diboson_1j1b",
    Type="OVERALL",
    Title='"Norm Diboson 1j1b"',
    OverallUp=0.25,
    OverallDown=-0.25,
    Samples="Diboson",
    Regions="reg1j1b",
    Category='"Norms"',
)

sys_diboson_norm_2j1b = block(
    "Systematic",
    "Norm_Diboson_2j1b",
    Type="OVERALL",
    Title='"Norm Diboson 2j1b"',
    OverallUp=0.25,
    OverallDown=-0.25,
    Samples="Diboson",
    Regions="reg2j1b",
    Category='"Norms"',
)

sys_diboson_norm_2j2b = block(
    "Systematic",
    "Norm_Diboson_2j2b",
    Type="OVERALL",
    Title='"Norm Diboson 2j2b"',
    OverallUp=0.25,
    OverallDown=-0.25,
    Samples="Diboson",
    Regions="reg2j2b",
    Category='"Norms"',
)

sys_diboson_norm_3j = block(
    "Systematic",
    "Norm_Diboson_3j",
    Type="OVERALL",
    Title='"Norm Diboson 3j"',
    OverallUp=0.25,
    OverallDown=-0.25,
    Samples="Diboson",
    Regions="reg3j",
    Category='"Norms"',
)


sys_mcnp_norm_1j1b = block(
    "Systematic",
    "Norm_MCNP_1j1b",
    Type="OVERALL",
    Title='"Norm MCNP 1j1b"',
    OverallUp=1.0,
    OverallDown=-1.0,
    Samples="MCNP",
    Regions="reg1j1b",
    Category='"Norms"',
)

sys_mcnp_norm_2j1b = block(
    "Systematic",
    "Norm_MCNP_2j1b",
    Type="OVERALL",
    Title='"Norm MCNP 2j1b"',
    OverallUp=1.0,
    OverallDown=-1.0,
    Samples="MCNP",
    Regions="reg2j1b",
    Category='"Norms"',
)

sys_mcnp_norm_2j2b = block(
    "Systematic",
    "Norm_MCNP_2j2b",
    Type="OVERALL",
    Title='"Norm MCNP 2j2b"',
    OverallUp=1.0,
    OverallDown=-1.0,
    Samples="MCNP",
    Regions="reg2j2b",
    Category='"Norms"',
)

sys_mcnp_norm_3j = block(
    "Systematic",
    "Norm_MCNP_3j",
    Type="OVERALL",
    Title='"Norm MCNP 3j"',
    OverallUp=1.0,
    OverallDown=-1.0,
    Samples="MCNP",
    Regions="reg3j",
    Category='"Norms"',
)

sys_zjets_norms = [sys_zjets_norm_1j1b, sys_zjets_norm_2j1b, sys_zjets_norm_2j2b, sys_zjets_norm_3j]

sys_diboson_norms = [
    sys_diboson_norm_1j1b,
    sys_diboson_norm_2j1b,
    sys_diboson_norm_2j2b,
    sys_diboson_norm_3j,
]

sys_mcnp_norms = [sys_mcnp_norm_1j1b, sys_mcnp_norm_2j1b, sys_mcnp_norm_2j2b, sys_mcnp_norm_3j]

sys_tW_DRDS = block(
    "Systematic",
    "tW_DRDS",
    Title='"tW DR vs DS"',
    Samples="tW",
    HistoNameSufUp='"_DS_FS"',
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
)

sys_tW_HS = block(
    "Systematic",
    "tW_HS",
    Title='"tW Hard Scatter"',
    Samples="tW",
    HistoNameSufUp='"_MCaNLO_AFII"',
    ReferenceSample="tWghost",
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
)

sys_tW_PS = block(
    "Systematic",
    "tW_PS",
    Title='"tW Parton Shower"',
    Samples="tW",
    HistoNameSufUp='"_H7_AFII"',
    ReferenceSample="tWghost",
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
    #NuisanceParameter='"PartonShower"',
)

sys_tW_AR = block(
    "Systematic",
    "tW_AR",
    Title='"tW Add. Radiation"',
    Samples="tW",
    HistoNameSufUp="_radHi",
    HistoNameSufDown="_radLo",
    Symmetrisation="TWOSIDED",
    Category="Modeling",
)

sys_ttbar_HS = block(
    "Systematic",
    "ttbar_HS",
    Title='"ttbar Hard Scatter"',
    Samples="ttbar",
    HistoNameSufUp='"_MCaNLO_AFII"',
    ReferenceSample="ttbarghost",
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
)

sys_ttbar_PS = block(
    "Systematic",
    "ttbar_PS",
    Title='"ttbar Parton Shower"',
    Samples="ttbar",
    HistoNameSufUp='"_H7_AFII"',
    ReferenceSample="ttbarghost",
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
    #NuisanceParameter='"PartonShower"',
)

sys_ttbar_AR = block(
    "Systematic",
    "ttbar_AR",
    Title='"ttbar Add. Radiation"',
    Samples="ttbar",
    HistoNameSufUp="_RU_AFII_radHi",
    HistoNameSufDown="_AFII_radLo",
    Symmetrisation="TWOSIDED",
    ReferenceSample="ttbarghost",
    Category='"Modeling"',
)


sys_tW_modeling = [sys_tW_DRDS, sys_tW_HS, sys_tW_PS, sys_tW_AR]
sys_ttbar_modeling = [sys_ttbar_HS, sys_ttbar_PS, sys_ttbar_AR]


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
            HistoNameSufUp='"_{}_Up"'.format(title),
            HistoNameSufDown='"_{}_Down"'.format(title),
            Symmetrisation="TWOSIDED",
            Category='"{}"'.format(category),
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)
        sys_weight_blocks.append(sysblock)
    return "".join(sys_weight_blocks)


def get_pdf_weights(do_smoothing=False):
    pdf_blocks = []
    for title, options in WtStat.systematics.PDF_WEIGHTS.items():
        if "90900" in title:
            continue
        upw = options[0]
        category = options[1]
        smoothing = options[2]
        sysblock = block(
            "Systematic",
            "{}".format(title),
            Title='"{}"'.format(title),
            Samples="tW,ttbar",
            HistoNameSufUp="_{}".format(title),
            Symmetrisation="ONESIDED",
            HistoNameSufUpRefSample="_PDFset90900",
            Category="PDFs",
            NuisanceParameter='"{}"'.format(title),
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
            Title='"{}"'.format(title.replace("_", " ")),
            Samples="tW,ttbar",
            HistoNameSufUp='"_{}"'.format(upt),
            HistoNameSufDown='"_{}"'.format(downt),
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
            Title='"{}"'.format(title.replace("_", " ")),
            Samples="tW,ttbar",
            HistoNameSufUp='"_{}"'.format(upt),
            Symmetrisation="ONESIDED",
            Category='"{}"'.format(category),
        )
        if do_smoothing and smoothing != 0:
            sysblock = "{}\n  Smoothing: {}".format(sysblock, smoothing)
        sys_tree_blocks.append(sysblock)
    return "".join(sys_tree_blocks)


def get_vrplots(yaml_file):
    def vrplot(region, variable, label, vtitle):
        bk = block(
            "Region",
            "VR_{}_{}".format(region, variable),
            Type="VALIDATION",
            Label='"{}"'.format(label),
            ShortLabel='"{}"'.format(label),
            HistoName='"{}_{}"'.format(region, variable),
            VariableTitle='"{}"'.format(vtitle),
        )
        return bk

    obj_kin_vrs = []
    with open(yaml_file, "r") as f:
        vr_yaml = yaml.load(f)
        vr_yaml = vr_yaml["templates"]
        for entry in vr_yaml:
            if entry["var"] == "bdt_response":
                continue
            filters = entry["filters"]
            if entry["filters"] == ["ALL"]:
                filters = ["reg1j1b", "reg2j1b", "reg2j2b", "reg3j"]
            for filt in filters:
                slabel = filt.split("_")[-1]
                var2plot = entry["var"]
                axtitle = entry["axis_title"]
                obj_kin_vrs.append(vrplot(filt, var2plot, slabel, axtitle))

    return "\n".join(obj_kin_vrs)
