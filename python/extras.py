from WtStat.trex import block


def vrplot(region, variable, label, vtitle):
    bk = block(
        "Region",
        "VR_{}_{}".format(region, variable),
        Type="VALIDATION",
        Label='"{}"'.format(label),
        ShortLabel='"{}"'.format(lable),
        HistoName='"{}_{}"'.format(region, variable),
        VariableTitle='"{}"'.format(vtitle),
    )
    return bk


obj_kin_vrs = []

obj_kin_vrs.append(vrplot("SR_1j1b", "pT_lep1", "1j1b", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_1j1b", "pT_lep2", "1j1b", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_1j1b", "pT_jet1", "1j1b", "#it{p}_{T}^{jet1} [GeV]"))

obj_kin_vrs.append(vrplot("SR_2j1b", "pT_lep1", "2j1b", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_lep2", "2j1b", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_jet1", "2j1b", "#it{p}_{T}^{jet1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j1b", "pT_jet2", "2j1b", "#it{p}_{T}^{jet2} [GeV]"))

obj_kin_vrs.append(vrplot("SR_2j2b", "pT_lep1", "2j2b", "#it{p}_{T}^{lep1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_lep2", "2j2b", "#it{p}_{T}^{lep2} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_jet1", "2j2b", "#it{p}_{T}^{jet1} [GeV]"))
obj_kin_vrs.append(vrplot("SR_2j2b", "pT_jet2", "2j2b", "#it{p}_{T}^{jet2} [GeV]"))

####### pTsys_lep1lep2jet1met
obj_kin_vrs.append(
    vrplot(
        "SR_1j1b",
        "pTsys_lep1lep2jet1met",
        "1j1b",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j1b",
        "pTsys_lep1lep2jet1met",
        "2j1b",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j2b",
        "pTsys_lep1lep2jet1met",
        "2j2b",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}#it{E}_{T}^{miss}) [GeV]",
    )
)

####### pTsys_lep1lep2jet1jet2met
obj_kin_vrs.append(
    vrplot(
        "SR_2j1b",
        "pTsys_lep1lep2jet1jet2met",
        "2j1b",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}j_{2}#it{E}_{T}^{miss}) [GeV]",
    )
)
obj_kin_vrs.append(
    vrplot(
        "SR_2j2b",
        "pTsys_lep1lep2jet1jet2met",
        "2j2b",
        "#it{p}_{T}^{sys}(l_{1}l_{2}_j_{1}j_{2}#it{E}_{T}^{miss}) [GeV]",
    )
)

####### pTsys_lep1lep2
obj_kin_vrs.append(
    vrplot("SR_1j1b", "pTsys_lep1lep2", "1j1b", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)
obj_kin_vrs.append(
    vrplot("SR_2j1b", "pTsys_lep1lep2", "2j1b", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)
obj_kin_vrs.append(
    vrplot("SR_2j2b", "pTsys_lep1lep2", "2j2b", "#it{p}_{T}^{sys}(l_{1}l_{2}) [GeV]")
)


obj_kin_vrs.append(vrplot("SR_2j2b", "minimaxmbl", "2j2b", "#it{m}_{bl}^{minimax}"))

obj_kin_vrs = "\n".join(obj_kin_vrs)
