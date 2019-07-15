from __future__ import print_function, division, absolute_import
import os
import shutil
import itertools
import subprocess
import WtStat.ntuple_trex


#ntupdir = "/Users/ddavis/ATLAS/data/bdt_main"
ntupdir = "/home/ddavis/ATLAS/data/bdt_main"
lumi = 140.5
name = "tW"
ncpu = 4

#master_3jpT_file = "/Users/ddavis/ATLAS/analysis/WtAna/WtStat/sandbox/tW_reg3jpT_histos.root"
master_3jpT_file = "/home/ddavis/ATLAS/analysis/WtAna/WtStat/sandbox/tW_reg3jpT_histos.root"

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

Systematic: "B_ev_B_0"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_up
  Title: "b-tag eigenv B0"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_down

Systematic: "B_ev_B_2"
  Category: "WeightBTag"
  WeightUp: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_up
  Title: "b-tag eigenv B2"
  Symmetrisation: TWOSIDED
  Samples: tW,ttbar
  WeightDown: weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_down

"""

post_constants = "".join(post_constants)
post_constants = "{}\n{}".format(post_constants, other_sys)


bdtv = range(22, 33, 4)
ptv = [26, 28, 30, 32]
r2j2b_max = [0.95]


bash_script = """#!/bin/bash

wt-stat ntupling -c fit.conf -r reg1j1b reg2j1b reg2j2b reg3jpT -m 4
trex-fitter wdf fit.conf
"""


for i, combo in enumerate(itertools.product(bdtv, bdtv, bdtv, ptv, r2j2b_max)):
    n1j1b, n2j1b, n2j2b, n3jpT, max2j2b = combo
    midblocks = []
    midblocks.append(WtStat.ntuple_trex.Region_1j1b(n1j1b, -0.70, 0.60))
    midblocks.append(WtStat.ntuple_trex.Region_2j1b(n2j1b, -0.70, 0.75))
    midblocks.append(WtStat.ntuple_trex.Region_2j2b(n2j2b, -0.85, max2j2b))
    midblocks.append(WtStat.ntuple_trex.Region_3jpT(n3jpT))

    config = "{}{}{}".format(pre_constants, "".join(midblocks), post_constants)

    dirname = "nbinscan95_{}_{}_{}_{}_{}_{}".format(str(i).zfill(4),
                                                  n1j1b, n2j1b, n2j2b, n3jpT, max2j2b)
    os.mkdir(dirname)
    with open("{}/fit.conf".format(dirname), "w") as f:
        f.write("{}{}{}".format(pre_constants, "".join(midblocks), post_constants))
    with open("{}/run.sh".format(dirname), "w") as f:
        f.write(bash_script.format(dirname))


items = []
for item in os.listdir('.'):
    if 'nbinscan95_' in item:
        items.append(item)

for i, item in enumerate(items):
    print(i, item)
    os.chdir(item)
    subprocess.call("bash run.sh", shell=True)
    os.chdir("..")


################################
################################

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
"""
