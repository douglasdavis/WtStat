#!/usr/bin/env python

from __future__ import print_function
import argparse
import os
from itertools import product
import subprocess
import WtStat.trex
import time

def hist_args(path):
    arg1 = "/".join(os.path.abspath(path).split("/")[:-1])
    arg2 = os.path.abspath(path).split("/")[-1].split(".root")[0]
    return '"{}"'.format(arg1), '"{}"'.format(arg2)


def make_combs(path):

    loe = []

    fileinfo = hist_args(path)

    Z = [6, 8, 12, 14, 16]
    for zconf in product(Z, Z, Z):
        z1j1b = zconf[0]
        z2j1b = zconf[1]
        z2j2b = zconf[2]

        for cut2j2b in [True, False]:
            if cut2j2b:
                r2j2b_func = WtStat.trex.Region_2j2bmblc_TransfoD
            else:
                r2j2b_func = WtStat.trex.Region_2j2b_TransfoD

            for crnj in [3, 4]:
                if crnj == 3:
                    cr_func = WtStat.trex.Region_3j
                else:
                    cr_func = WtStat.trex.Region_4j

                name = "{hname}_{zinfo}_{cutinfo}_{crinfo}".format(
                    hname=fileinfo[1][1:-1],
                    zinfo="{}{}{}".format(z1j1b, z2j1b, z2j2b),
                    cutinfo="cut" if cut2j2b else "nocut",
                    crinfo=crnj,
                )


                conffilename = "{}.conf".format(name)

                outtext = []

                outtext.append(WtStat.trex.Job(name, fileinfo[0], fileinfo[1], 140.5))
                outtext.append(WtStat.trex.Fit(name, blind="TRUE"))

                outtext.append(WtStat.trex.Region_1j1b_TransfoD(z1j1b, z1j1b))
                outtext.append(WtStat.trex.Region_2j1b_TransfoD(z2j1b, z2j1b))
                outtext.append(r2j2b_func(z2j2b, z2j2b))
                outtext.append(cr_func())

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

                with open(conffilename, 'w') as f:
                    f.write(''.join(outtext))

                loe.append("trex-fitter hwdf {}".format(conffilename))

    return list(reversed(loe))

def main():
    parser = argparse.ArgumentParser(description="sandbox")
    parser.add_argument(
        "-f", dest="hfile", type=str, help="histograms file", required=True
    )
    args = parser.parse_args()

    loe = make_combs(args.hfile)
    total_jobs = len(loe)
    total_done = 0

    def done(p):
        return p.poll() is not None
    def success(p):
        return p.returncode == 0
    def fail():
        sys.exit(1)

    max_task = 4
    processes = []

    while True:
        while loe and len(processes) < max_task:
            ex = loe.pop()
            print(ex)
            nameroot = ex.split('hwdf ')[-1].split('.conf')[0]
            stdoutname = '{}.stdout.log'.format(nameroot)
            stderrname ='{}.stderr.log'.format(nameroot)
            with open(stdoutname, 'w') as sout, open(stderrname, 'w') as serr:
                processes.append(subprocess.Popen(ex, shell=True, stdout=sout, stderr=serr))

        for p in processes:
            if done(p):
                if success(p):
                    total_done += 1
                    print('{}/{}'.format(total_done, total_jobs))
                    processes.remove(p)

        if not processes and not loe:
            break
        else:
            time.sleep(0.05)

    return 0


if __name__ == "__main__":
    main()
