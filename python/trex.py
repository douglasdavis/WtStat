import WtStat.systematics


def block(block_type, block_title, **options):
    ret = '{}: "{}"'.format(block_type, block_title)
    for k, v in options.items():
        ret = "{}\n  {}: {}".format(ret, k, v)
    return "{}\n".format(ret)


def Job(name, hpath, hfile):
    bk = block(
        "Job",
        name,
        CmeLabel='"13 TeV"',
        POI='"SigXsecOverSM"',
        ReadFrom="HIST",
        HistoPath=hpath,
        HistoFile=hfile,
        DebugLevel=1,
        MCstatThreshold=0.001,
        SystControlPlots="TRUE",
        SystPruningShape=0.005,
        SystPruningNorm=0.005,
        ImageFormat='"pdf"',
        SystCategoryTables="TRUE",
        RankingPlot="all",
        RankingMaxNP=15,
        DoSummaryPlot="TRUE",
        DoTables="TRUE",
        DoSignalRegionsPlot="TRUE",
        DoPieChartPlot="True",
    )
    return bk


def Fit(name, blind="TRUE"):
    bk = block(
        "Fit",
        name,
        FitType="SPLUSB",
        FitRegion="CRSR",
        NumCPU="4",
        POIAsimov=1,
        FitBlind=blind,
    )
    return bk


def Region_1j1b_TransfoD(zs=5, zb=5):
    bk = block(
        "Region",
        "reg1j1b",
        Type="SIGNAL",
        Label="1j1b",
        ShortLabel="1j1b",
        HistoName='"SR_1j1b_bdt_response"',
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
        HistoName='"SR_2j1b_bdt_response"',
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
        HistoName='"SR_2j2b_bdt_response"',
        Binning='"AutoBin","TransfoD",{zs},{zb}'.format(zs=zs, zb=zb),
    )
    return bk


def Region_2j2bmblc_TransfoD(zs=5, zb=5):
    bk = block(
        "Region",
        "reg2j2b",
        Type="SIGNAL",
        Label="2j2b",
        ShortLabel="2j2b",
        HistoName='"SR_2j2bmblc_bdt_response"',
        Binning='"AutoBin","TransfoD",{zs},{zb}'.format(zs=zs, zb=zb),
    )
    return bk


def Region_3j():
    bk = block(
        "Region",
        "reg3j",
        Type="CONTROL",
        Label="3j",
        ShortLabel="3j",
        HistoName='"CR_3j_pT_jet2"',
    )
    return bk


_tWghost = block("Sample", "tWghost", Type="GHOST", HistoNameSuff='"_tW_AFII"')
_ttbarghost = block("Sample", "ttbarghost", Type="GHOST", HistoNameSuff='"_ttbar_AFII"')

ghost_samples = "{}\n{}".format(_tWghost, _ttbarghost)

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
    TexTitle='"$t\bar{t}$"',
    FillColor=633,
    LineColor=1,
    Type="BACKGROUND",
    HistoNameSuff='"_ttbar"',
)

Zjets_sample = block(
    "Sample",
    "Zjets",
    Title='"#it{Z}+jets"',
    TexTitle="Z + jets",
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
    OverallUp=0.023,
    OverallDown=-0.023,
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
    Samples="Diboson",
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
    Samples="Diboson",
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
    Samples="Diboson",
    Regions="reg2j2b",
    Category='"Norms"',
)

sys_diboson_norm_1j1b = block(
    "Systematic",
    "Norm_Diboson_1j1b",
    Type="OVERALL",
    Title='"Norm Diboson 1j1b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Diboson",
    Regions="reg1j1b",
    Category='"Norms"',
)

sys_diboson_norm_2j1b = block(
    "Systematic",
    "Norm_Diboson_2j1b",
    Type="OVERALL",
    Title='"Norm Diboson 2j1b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Diboson",
    Regions="reg2j1b",
    Category='"Norms"',
)

sys_diboson_norm_2j2b = block(
    "Systematic",
    "Norm_Diboson_2j2b",
    Type="OVERALL",
    Title='"Norm Diboson 2j2b"',
    OverallUp=0.5,
    OverallDown=-0.5,
    Samples="Diboson",
    Regions="reg2j2b",
    Category='"Norms"',
)

sys_tW_DRDS = block(
    "Systematic",
    "tW_DRDS",
    Title='"tW DR vs DS"',
    Samples="tW",
    HistoNameSufUp='"_DS_FS"',
    Symmetrisation="ONESIDED",
    Category='"Modeling"',
)
