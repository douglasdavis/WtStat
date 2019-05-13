from __future__ import print_function, division, absolute_import
import os
import itertools
import WtStat.ntuple_trex

ntupdir = "/var/phy/project/hep/atlas/users/drd25/data/wtloop/v28_20190501/bdt_main"
lumi = 140.5
name = "tW"
ncpu = 8

pre_constants = []
pre_constants.append(WtStat.ntuple_trex.Job(name, ntupdir, lumi))
pre_constants.append(WtStat.ntuple_trex.Fit(name, blind="TRUE", NumCPU=ncpu))
pre_constants = "".join(pre_constants)

post_constants = []
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.Sample_tWghost(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_ttbarghost(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_tWpdfghost(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_ttbarpdfghost(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_Data(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_tW(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_ttbar(ntupdir))
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.Sample_Zjets(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_Diboson(ntupdir))
post_constants.append(WtStat.ntuple_trex.Sample_MCNP(ntupdir))
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.NF_tW())
post_constants.append(WtStat.ntuple_trex.NF_ttbar())
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.Systematic_lumi())
post_constants.append(WtStat.ntuple_trex.Systematic_tW_DRDS(ntupdir))
post_constants.append(WtStat.ntuple_trex.Systematic_tW_PS(ntupdir))
post_constants.append(WtStat.ntuple_trex.Systematic_tW_HS(ntupdir))
post_constants.append(WtStat.ntuple_trex.Systematic_tW_AR())
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.Systematic_ttbar_PS(ntupdir))
post_constants.append(WtStat.ntuple_trex.Systematic_ttbar_HS(ntupdir))
post_constants.append(WtStat.ntuple_trex.Systematic_ttbar_AR(ntupdir))
post_constants.append("\n")
post_constants.append(WtStat.ntuple_trex.NF_minor(regions=["1j1b","2j1b","2j2b","3jpT"]))

other_sys = """
Systematic: "Jet_JER_EffNP_2"
  Category: "JER"
  Title: "JetJEREffNP2"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_JER_EffectiveNP_2__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_JER_EffectiveNP_2__1up.bdt_response

Systematic: "Jet_Flavor_Response"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_Flavor_Response__1down.bdt_response
  Title: "JetFlavorResponse"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_Flavor_Response__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_Flavor_Response__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_Flavor_Response__1down

Systematic: "MET_SoftTrk_Scale"
  Category: "MET"
  NtupleFileSufDown: _MET_SoftTrk_ScaleDown.bdt_response
  Title: "METSoftTrkScale"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_MET_SoftTrk_ScaleUp
  NtupleFileSufUp: _MET_SoftTrk_ScaleUp.bdt_response
  NtupleNameDown: WtTMVA_MET_SoftTrk_ScaleDown

Systematic: "Jet_Pileup_RhoTopology"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_Pileup_RhoTopology__1down.bdt_response
  Title: "JetPileupRhoTopology"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_Pileup_RhoTopology__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_Pileup_RhoTopology__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_Pileup_RhoTopology__1down

Systematic: "B_ev_B_0"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_up
  Title: "b-tag eigenv B0"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_down

Systematic: "Jet_EtaIntercal_Modelling"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1down.bdt_response
  Title: "JetEtaIntercalModelling"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1down

Systematic: "MET_SoftTrk_ResoPerp"
  Category: "MET"
  Title: "METSoftTrkResoPerp"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_MET_SoftTrk_ResoPerp
  NtupleFileSufUp: _MET_SoftTrk_ResoPerp.bdt_response

Systematic: "B_ev_B_4"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_4_up
  Title: "b-tag eigenv B4"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_4_down

Systematic: "Jet_EffNP_Modelling1"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_EffectiveNP_Modelling1__1down.bdt_response
  Title: "JetEffNPModelling1"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Modelling1__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_EffectiveNP_Modelling1__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Modelling1__1down

Systematic: "EL_ID"
  Category: "WeightLepSFs"
  WeightUp: weight_sys_leptonSF_EL_SF_ID_UP
  Title: "Electron ID"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_leptonSF_EL_SF_ID_DOWN

Systematic: "Jet_JER_EffNP_3"
  Category: "JER"
  Title: "JetJEREffNP3"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_JER_EffectiveNP_3__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_JER_EffectiveNP_3__1up.bdt_response

Systematic: "EG_SCALE_ALL"
  Category: "Egamma"
  NtupleFileSufDown: _EG_SCALE_ALL__1down.bdt_response
  Title: "EGSCALEALL"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_EG_SCALE_ALL__1up
  NtupleFileSufUp: _EG_SCALE_ALL__1up.bdt_response
  NtupleNameDown: WtTMVA_EG_SCALE_ALL__1down

Systematic: "B_ev_B_5"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_5_up
  Title: "b-tag eigenv B5"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_5_down

Systematic: "Jet_JER_EffNP_1"
  Category: "JER"
  Title: "JetJEREffNP1"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_JER_EffectiveNP_1__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_JER_EffectiveNP_1__1up.bdt_response

Systematic: "B_ev_L_0"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_0_up
  Title: "b-tag eigenv L0"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_0_down

Systematic: "Jet_BJES_Response"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_BJES_Response__1down.bdt_response
  Title: "JetBJESResponse"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_BJES_Response__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_BJES_Response__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_BJES_Response__1down

Systematic: "Jet_EffNP_Modelling2"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_EffectiveNP_Modelling2__1down.bdt_response
  Title: "JetEffNPModelling2"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Modelling2__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_EffectiveNP_Modelling2__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Modelling2__1down

Systematic: "Jet_JER_EffectiveNP_7restTerm"
  Category: "JER"
  Title: "JetJEREffectiveNP7restTerm"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_JER_EffectiveNP_7restTerm__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_JER_EffectiveNP_7restTerm__1up.bdt_response

Systematic: "Pileup"
  Category: "Weights"
  WeightUp: weight_sys_pileup_UP
  Title: "Pileup"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_pileup_DOWN

Systematic: "Jet_JER_EffNP_4"
  Category: "JER"
  Title: "JetJEREffNP4"
  Symmetrisation: ONESIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_JER_EffectiveNP_4__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_JER_EffectiveNP_4__1up.bdt_response

Systematic: "Jet_EtaIntercal_TotalStat"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1down.bdt_response
  Title: "JetEtaIntercalTotalStat"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1down

Systematic: "B_ev_B_2"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_up
  Title: "b-tag eigenv B2"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_down

Systematic: "B_ev_B_2"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_up
  Title: "b-tag eigenv B2"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_down

Systematic: "B_ev_B_6"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_6_up
  Title: "b-tag eigenv B6"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_6_down

Systematic: "B_ev_B_7"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_7_up
  Title: "b-tag eigenv B7"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_7_down

Systematic: "B_ev_B_1"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_1_up
  Title: "b-tag eigenv B1"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_1_down

Systematic: "Jet_Pileup_OffsetMu"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_Pileup_OffsetMu__1down.bdt_response
  Title: "JetPileupOffsetMu"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_Pileup_OffsetMu__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_Pileup_OffsetMu__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_Pileup_OffsetMu__1down

Systematic: "Jet_EffNP_Mixed2"
  Category: "Jets"
  NtupleFileSufDown: _JET_CategoryReduction_JET_EffectiveNP_Mixed2__1down.bdt_response
  Title: "JetEffNPMixed2"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  NtupleNameUp: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Mixed2__1up
  NtupleFileSufUp: _JET_CategoryReduction_JET_EffectiveNP_Mixed2__1up.bdt_response
  NtupleNameDown: WtTMVA_JET_CategoryReduction_JET_EffectiveNP_Mixed2__1down
"""

post_constants = "".join(post_constants)
post_constants = "{}\n{}".format(post_constants, other_sys)


def gen_combos(lo, hi, n):
    coms = [(lo, hi)]
    zs, zb = lo + 1, hi - 1
    while zs <= hi and zb >= lo:
        if zs > zb:
            pass
        else:
            coms.append((zs, zb))
        zs += n
        zb -= n
    #coms.append((hi, lo))
    return coms

combos_1j1b = gen_combos(0, 23, 2)
combos_2j1b = gen_combos(0, 23, 2)
combos_2j2b = gen_combos(0, 27, 2)

bash_script = """
#!/bin/bash

wt-stat ntupling -c fit.conf -r reg1j1b reg2j1b reg2j2b reg3jpT -m 4
trex-fitter wdf fit.conf
"""


for i, combo in enumerate(itertools.product(combos_1j1b, combos_2j1b, combos_2j2b)):
    opt_1j1b, opt_2j1b, opt_2j2b = combo


    midblocks = []
    midblocks.append(WtStat.ntuple_trex.Region_1j1b(23, -0.70, 0.60, zs=opt_1j1b[0], zb=opt_1j1b[1]))
    midblocks.append(WtStat.ntuple_trex.Region_2j1b(23, -0.70, 0.75, zs=opt_2j1b[0], zb=opt_2j1b[1]))
    midblocks.append(WtStat.ntuple_trex.Region_2j2b(27, -0.85, 0.95, zs=opt_2j2b[0], zb=opt_2j2b[1]))
    midblocks.append(WtStat.ntuple_trex.Region_3jpT(30))

    config = "{}{}{}".format(pre_constants, "".join(midblocks), post_constants)

    dirname = "fitbinscan_{}__{}-{}_{}-{}_{}-{}".format(str(i).zfill(4),
                                                        opt_1j1b[0], opt_1j1b[1],
                                                        opt_2j1b[0], opt_2j1b[1],
                                                        opt_2j2b[0], opt_2j2b[1])
    os.mkdir(dirname)
    with open("{}/fit.conf".format(dirname), "w") as f:
        f.write("{}{}{}".format(pre_constants, "".join(midblocks), post_constants))
    with open("{}/run.sh".format(dirname), "w") as f:
        f.write(bash_script)

    #if i > 20:
    #    break
