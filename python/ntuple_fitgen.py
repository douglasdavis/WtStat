from __future__ import print_function
import os
import WtStat.ntuple_trex


def ntuple_fit(
    name,
    ntupdir,
    outdir,
    lumi=140.5,
    ncpu=6,
    blind=True,
    skip_treesys=False,
    skip_weightsys=False,
    skip_pdfs=False,
    vrplots=None,
    regions=["1j1b", "2j1b", "2j2b", "3jpT"],
):
    outtext = []

    ## job and fit blocks

    outtext.append(WtStat.ntuple_trex.Job(name, ntupdir, lumi))
    outtext.append(WtStat.ntuple_trex.Fit(name, blind="TRUE" if blind else "FALSE", NumCPU=ncpu))

    r1j1b = WtStat.ntuple_trex.Region_1j1b(36, -0.70, 0.60)
    r2j1b = WtStat.ntuple_trex.Region_2j1b(22, -0.70, 0.75)
    r2j2b = WtStat.ntuple_trex.Region_2j2b(34, -0.85, 0.90)
    r3jpT = WtStat.ntuple_trex.Region_3jpT(34)

    ## region blocks
    if "nominal" in regions:
        outtext += [r1j1b, r2j1b, r2j2b, r3jpT]
    else:
        if "1j1b" in regions:
            outtext.append(r1j1b)
        if "2j1b" in regions:
            outtext.append(r2j1b)
        if "2j2b" in regions:
            outtext.append(r2j2b)
        if "3jpT" in regions:
            outtext.append(r3jpT)

    ## sample blocks
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.Sample_tWghost(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_ttbarghost(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_tWpdfghost(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_ttbarpdfghost(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_Data(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_tW(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_ttbar(ntupdir))
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.Sample_Zjets(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_Diboson(ntupdir))
    outtext.append(WtStat.ntuple_trex.Sample_MCNP(ntupdir))
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.NF_tW())
    outtext.append(WtStat.ntuple_trex.NF_ttbar())
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.Systematic_lumi())
    outtext.append(WtStat.ntuple_trex.Systematic_tW_DRDS(ntupdir))
    outtext.append(WtStat.ntuple_trex.Systematic_tW_PS(ntupdir))
    outtext.append(WtStat.ntuple_trex.Systematic_tW_HS(ntupdir))
    outtext.append(WtStat.ntuple_trex.Systematic_tW_AR())
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.Systematic_ttbar_PS(ntupdir))
    outtext.append(WtStat.ntuple_trex.Systematic_ttbar_HS(ntupdir))
    outtext.append(WtStat.ntuple_trex.Systematic_ttbar_AR(ntupdir))
    outtext.append("\n")
    #outtext.append(WtStat.ntuple_trex.NF_minor(regions=["1j1b","2j1b","2j2b","3j1b"]))
    outtext.append(WtStat.ntuple_trex.NF_minor_inclusive())
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.get_sys_weights())
    outtext.append(WtStat.ntuple_trex.get_sys_trees2s())
    outtext.append(WtStat.ntuple_trex.get_sys_trees1s())
    #outtext.append(WtStat.ntuple_trex.get_tW_pdf_weights())
    #outtext.append(WtStat.ntuple_trex.get_ttbar_pdf_weights())

    # print(outtext)

    os.mkdir(outdir)

    with open("{}/fit.conf".format(outdir), "w") as f:
        f.write("".join(outtext))
