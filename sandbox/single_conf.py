import WtStat.trex

print WtStat.trex.Job("tWfit", '"/Users/ddavis/Desktop"', '"histograms_lumifix"', 140.5)
print WtStat.trex.Fit("tWfit", blind="TRUE")

print WtStat.trex.Region_1j1b_TransfoD(7,7)
print WtStat.trex.Region_2j1b_TransfoD(4,4)
print WtStat.trex.Region_2j2bmblc_TransfoD(6,6)
print WtStat.trex.Region_3j(rebin=0)

#print WtStat.trex.Region_1j1b()
#print WtStat.trex.Region_2j1b()
#print WtStat.trex.Region_2j2bmblc()
#print WtStat.trex.Region_3j()

print WtStat.trex.ghost_samples
print WtStat.trex.data_sample
print WtStat.trex.tW_sample
print WtStat.trex.ttbar_sample
print WtStat.trex.Zjets_sample
print WtStat.trex.Diboson_sample
print WtStat.trex.MCNP_sample

print WtStat.trex.tW_NF
print WtStat.trex.ttbar_NF

print WtStat.trex.sys_lumi

print WtStat.trex.sys_zjets_norm_1j1b
print WtStat.trex.sys_zjets_norm_2j1b
print WtStat.trex.sys_zjets_norm_2j2b

print WtStat.trex.sys_diboson_norm_1j1b
print WtStat.trex.sys_diboson_norm_2j1b
print WtStat.trex.sys_diboson_norm_2j2b

print WtStat.trex.sys_tW_DRDS
print WtStat.trex.sys_tW_HS
print WtStat.trex.sys_tW_PS
print WtStat.trex.sys_tW_AR

print WtStat.trex.sys_ttbar_HS
print WtStat.trex.sys_ttbar_PS
print WtStat.trex.sys_ttbar_AR

print WtStat.trex.get_sys_weights(do_smoothing=False)
print WtStat.trex.get_sys_trees2s(do_smoothing=False)
print WtStat.trex.get_sys_trees1s(do_smoothing=False)
