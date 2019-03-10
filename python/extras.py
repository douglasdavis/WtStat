from WtStat.trex import block


def vrplot(region, variable, vtitle):
    bk = block(
        "Region",
        "VR_{}_{}".format(region, variable),
        Type="VALIDATION",
        Label="a",  # '"{}_{}"'.format(region, variable),
        ShortLabel="b",  # '"{}_{}"'.format(region, variable),
        HistoName='"{}_{}"'.format(region, variable),
        VariableTitle='"{}"'.format(vtitle),
    )
    return bk


obj_kin_vrs = []

obj_kin_vrs.append(vrplot("SR_1j1b", "pT_lep1", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_1j1b", "pT_lep2", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_1j1b", "pT_jet1", "#it{p}_{T}^{jet1} [GeV]"))

obj_kin_vrs.append(vrplot("SR_2j1b", "pT_lep1", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_lep2", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_jet1", "#it{p}_{T}^{jet1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_jet2", "#it{p}_{T}^{jet2} [GeV]"))

obj_kin_vrs.append(vrplot("SR_2j2b", "pT_lep1", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_lep2", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_jet1", "#it{p}_{T}^{jet1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_jet2", "#it{p}_{T}^{jet2} [GeV]"))

####### pTsys_lep1lep2jet1met
obj_kin_vrs.append(
    vrplot(
        "SR_1j1b",
        "pTsys_lep1lep2jet1met",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j1b",
        "pTsys_lep1lep2jet1met",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j2b",
        "pTsys_lep1lep2jet1met",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)

####### pTsys_lep1lep2jet1jet2met
obj_kin_vrs.append(
    vrplot(
        "SR_2j1b",
        "pTsys_lep1lep2jet1jet2met",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}j_{2}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j2b",
        "pTsys_lep1lep2jet1jet2met",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}j_{2}#it{E}_{T}^{miss}) [GeV]",
    )
)

####### pTsys_lep1lep2
obj_kin_vrs.append(
    vrplot("SR_1j1b", "pTsys_lep1lep2", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)
obj_kin_vrs.append(
    vrplot("SR_2j1b", "pTsys_lep1lep2", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)
obj_kin_vrs.append(
    vrplot("SR_2j2b", "pTsys_lep1lep2", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)


obj_kin_vrs.append(vrplot("SR_2j2b", "minimaxmbl", "#it{m}_{bl}^{minimax}"))

obj_kin_vrs = "\n".join(obj_kin_vrs)
