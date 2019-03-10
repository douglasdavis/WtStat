import os
import WtStat.trex
import WtStat.extras
from WtStat.utils import hfilesplit


def fit_workspace(
    name, hfile, outdir, lumi=140.5, ncpu=2, blind=True, do_vrplots=False
):
    fileinfo = hfilesplit(hfile)

    outtext = []

    ## `Job` and `Fit` blocks
    outtext.append(WtStat.trex.Job(name, fileinfo[0], fileinfo[1], lumi))
    outtext.append(WtStat.trex.Fit(name, blind="TRUE" if blind else "FALSE"))

    ## `Region` blocks
    outtext.append(WtStat.trex.Region_1j1b(rebin=2))
    outtext.append(WtStat.trex.Region_2j1b(rebin=2))
    outtext.append(WtStat.trex.Region_2j2b(rebin=2))
    outtext.append(WtStat.trex.Region_3j(rebin=2))

    if do_vrplots:
        outtext.append(WtStat.extras.obj_kin_vrs)

    ## shortcut for all `Samples` blocks
    outtext += WtStat.trex.all_samples

    ## `NormFactor` blocks
    outtext.append(WtStat.trex.tW_NF)
    outtext.append(WtStat.trex.ttbar_NF)

    ## lumi `Systematic` block
    outtext.append(WtStat.trex.sys_lumi)

    ## All modeling `Systematic` blocks
    outtext += WtStat.trex.sys_tW_modeling
    outtext += WtStat.trex.sys_ttbar_modeling
    outtext += WtStat.trex.sys_diboson_norms
    outtext += WtStat.trex.sys_zjets_norms
    outtext += WtStat.trex.sys_mcnp_norms

    ## Shortcuts for all tree/weight `Systematic` blocks
    outtext.append(WtStat.trex.get_sys_weights(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees2s(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees1s(do_smoothing=False))

    os.mkdir(outdir)

    with open("{}/fit.conf".format(outdir), "w") as f:
        f.write("".join(outtext))
