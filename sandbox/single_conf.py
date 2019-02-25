#!/usr/bin/env python

from __future__ import print_function
import argparse
import os
import WtStat.trex


def main():
    parser = argparse.ArgumentParser(description='sandbox')
    parser.add_argument('-n', dest='name', type=str, help='fit name', required=True)
    parser.add_argument('-f', dest='hfile', type=str, help='histograms file', required=True)
    parser.add_argument('-l', dest='lumi', type=float, help='lumi', required=False, default=140.5)
    parser.add_argument('-o', dest='outname', type=str, help='output config file name', required=False, default='tWfit.conf')
    parser.add_argument('-r', dest='runopts', type=str, help="run options", required=False)
    args = parser.parse_args()

    fileinfo = hist_args(args.hfile)

    outtext = []

    outtext.append(WtStat.trex.Job(args.name, fileinfo[0], fileinfo[1], args.lumi))
    outtext.append(WtStat.trex.Fit(args.name, blind="TRUE"))

    outtext.append(WtStat.trex.Region_1j1b_TransfoD(16,0))
    outtext.append(WtStat.trex.Region_2j1b_TransfoD(16,0))
    outtext.append(WtStat.trex.Region_2j2bmblc_TransfoD(14,0))
    outtext.append(WtStat.trex.Region_3j(rebin=0))

    #outtext.append(WtStat.trex.Region_1j1b(2))
    #outtext.append(WtStat.trex.Region_2j1b(2))
    #outtext.append(WtStat.trex.Region_2j2bmblc(2))
    #outtext.append(WtStat.trex.Region_3j(rebin=0))

    outtext += WtStat.trex.all_samples

    outtext.append(WtStat.trex.tW_NF)
    outtext.append(WtStat.trex.ttbar_NF)

    outtext.append(WtStat.trex.sys_lumi)

    outtext += WtStat.trex.sys_tW_modeling
    outtext += WtStat.trex.sys_ttbar_modeling
    outtext += WtStat.trex.sys_diboson_norms
    outtext += WtStat.trex.sys_zjets_norms

    outtext.append(WtStat.trex.get_sys_weights(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees2s(do_smoothing=False))
    outtext.append(WtStat.trex.get_sys_trees1s(do_smoothing=False))

    with open(args.outname, 'w') as f:
        f.write(''.join(outtext))

    if args.runopts:
        import subprocess
        subprocess.call('echo "trex-fitter {0} {1}" > {1}.sh'.format(args.runopts, args.outname), shell=True)
        subprocess.call(['bash','{}.sh'.format(args.outname)])

if __name__ == '__main__':
    main()
