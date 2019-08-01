#!/usr/bin/env python

import argparse
import uproot
import numpy as np

# fmt: off
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from root_numpy import array2hist
# fmt: on

SIG_SAMPLES = ["tW"]
BKG_SAMPLES = ["ttbar", "Diboson", "Zjets", "MCNP"]
DEFAULT_REGIONS = [
    "reg1j1b_bdt_response",
    "reg2j1b_bdt_response",
    "reg2j2b_bdt_response",
    "reg3j_bdt_response_3j",
]


def get_keepers(urhfile, region, target=10):
    nbins = urhfile.get(f"{region}_Data").numbins
    sigsum = np.zeros((nbins), dtype=np.float64)
    bkgsum = np.zeros((nbins), dtype=np.float64)
    for signame in SIG_SAMPLES:
        sigsum += urhfile.get(f"{region}_{signame}").values
    for bkgname in BKG_SAMPLES:
        bkgsum += urhfile.get(f"{region}_{bkgname}").values
    soverb = np.round(sigsum / bkgsum, 3) * 100
    return np.argwhere(soverb < target).flatten()


def get_args():
    # fmt: off
    parser = argparse.ArgumentParser(description="select bins based on S/B")
    parser.add_argument("histogramfile", type=str, help="File containing histograms")
    parser.add_argument("regions", type=str, nargs="+", help="Which regions to parse")
    parser.add_argument("outfile", type=str, help="output ROOT file")
    parser.add_argument("target", type=float, default=10, help="S/B target cutoff")
    # fmt: on
    return parser.parse_args()


def main():
    args = get_args()
    urhfile = uproot.open(args.histogramfile)
    rrfile = ROOT.TFile.Open(args.outfile, "RECREATE")
    rrfile.cd()
    regions = args.regions
    if regions == ["_all"]:
        regions = DEFAULT_REGIONS
    for region in regions:
        keepers = get_keepers(urhfile, region, target=args.target)
        print(f"{region}:\t {keepers}")
        for k in urhfile.keys():
            key = k.decode('utf-8')
            if ";" in key:
                key = key.split(";")[0]
            if region in key:
                urhist = urhfile.get(key)
                count = urhist.values
                sumw2 = urhist.variances
                countkeep = np.zeros((keepers.shape[0] + 2))
                sumw2keep = np.zeros((keepers.shape[0] + 2))
                countkeep[1:-1] = count[keepers]
                sumw2keep[1:-1] = sumw2[keepers]
                rrhist = ROOT.TH1D(key, key, len(keepers), 0, 1)
                array2hist(countkeep, rrhist, np.sqrt(sumw2keep))
                rrhist.Write("", ROOT.TObject.kOverwrite)
                rrhist.SetDirectory(0)
    rrfile.Close()


if __name__ == "__main__":
    main()
