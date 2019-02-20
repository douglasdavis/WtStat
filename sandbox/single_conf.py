#!/usr/bin/env python

from __future__ import print_function
import argparse
import WtStat.trex

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

def hist_args(path):
    p = pathlib.Path(path).resolve()
    arg1 = str(p.parent)
    arg2 = p.name.split('.root')[0]
    return '"{}"'.format(arg1), '"{}"'.format(arg2)

def main():
    parser = argparse.ArgumentParser(description='sandbox')
    parser.add_argument('-n', dest='name', type=str, help='fit name', required=True)
    parser.add_argument('-f', dest='hfile', type=str, help='histograms file', required=True)
    parser.add_argument('-l', dest='lumi', type=float, help='lumi', required=False, default=140.5)
    parser.add_argument('-o', dest='outname', type=str, help='output config file name', required=False, default='tWfit.conf')
    args = parser.parse_args()

    fileinfo = hist_args(args.hfile)

    outtext = []

    outtext.append(WtStat.trex.Job(args.name, fileinfo[0], fileinfo[1], args.lumi))
    outtext.append(WtStat.trex.Fit(args.name, blind="TRUE"))

    outtext.append(WtStat.trex.Region_1j1b_TransfoD(7,7))
    outtext.append(WtStat.trex.Region_2j1b_TransfoD(4,4))
    outtext.append(WtStat.trex.Region_2j2bmblc_TransfoD(6,6))
    outtext.append(WtStat.trex.Region_3j(rebin=0))

    #outtext.append(WtStat.trex.Region_1j1b()
    #outtext.append(WtStat.trex.Region_2j1b()
    #outtext.append(WtStat.trex.Region_2j2bmblc()
    #outtext.append(WtStat.trex.Region_3j()

    outtext.append(WtStat.trex.ghost_samples)
    outtext.append(WtStat.trex.data_sample)
    outtext.append(WtStat.trex.tW_sample)
    outtext.append(WtStat.trex.ttbar_sample)
    outtext.append(WtStat.trex.Zjets_sample)
    outtext.append(WtStat.trex.Diboson_sample)
    outtext.append(WtStat.trex.MCNP_sample)

    outtext.append(WtStat.trex.tW_NF)
    outtext.append(WtStat.trex.ttbar_NF)

    outtext.append(WtStat.trex.sys_lumi)

    outtext.append(WtStat.trex.sys_zjets_norm_1j1b)
    outtext.append(WtStat.trex.sys_zjets_norm_2j1b)
    outtext.append(WtStat.trex.sys_zjets_norm_2j2b)

    outtext.append(WtStat.trex.sys_diboson_norm_1j1b)
    outtext.append(WtStat.trex.sys_diboson_norm_2j1b)
    outtext.append(WtStat.trex.sys_diboson_norm_2j2b)

    outtext.append(WtStat.trex.sys_tW_DRDS)
    outtext.append(WtStat.trex.sys_tW_HS)
    outtext.append(WtStat.trex.sys_tW_PS)
    outtext.append(WtStat.trex.sys_tW_AR)

    outtext.append(WtStat.trex.sys_ttbar_HS)
    outtext.append(WtStat.trex.sys_ttbar_PS)
    outtext.append(WtStat.trex.sys_ttbar_AR)

    outtext.append(WtStat.trex.get_sys_weights(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees2s(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees1s(do_smoothing=False))

    outfile = pathlib.Path(args.outname)
    outfile.write_text(''.join(outtext))

if __name__ == '__main__':
    main()
