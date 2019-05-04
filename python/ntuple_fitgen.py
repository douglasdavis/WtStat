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
):
    outtext = []

    ## job and fit blocks

    outtext.append(WtStat.ntuple_trex.Job(name, ntupdir, lumi))
    outtext.append(WtStat.ntuple_trex.Fit(name, blind="TRUE" if blind else "FALSE"))

    ## region blocks

    outtext.append(WtStat.ntuple_trex.Region_1j1b())
    outtext.append(WtStat.ntuple_trex.Region_2j1b())
    outtext.append(WtStat.ntuple_trex.Region_2j2b())
    #outtext.append(WtStat.ntuple_trex.Region_3jpT())
    outtext.append(WtStat.ntuple_trex.Region_3j1b())
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
    outtext.append(WtStat.ntuple_trex.NF_minor())
    outtext.append("\n")
    outtext.append(WtStat.ntuple_trex.get_sys_weights())
    outtext.append(WtStat.ntuple_trex.get_tW_pdf_weights())
    outtext.append(WtStat.ntuple_trex.get_ttbar_pdf_weights())
    outtext.append(WtStat.ntuple_trex.get_sys_trees2s())
    outtext.append(WtStat.ntuple_trex.get_sys_trees1s())

    # print(outtext)

    os.mkdir(outdir)

    with open("{}/fit.conf".format(outdir), "w") as f:
        f.write("".join(outtext))
