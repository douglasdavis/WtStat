#!/usr/bin/env python3

"""
Script to make matplotlib plots from TRExFitter output. Requires
at least Python 3.7

ddavis@cern.ch
"""

from __future__ import annotations

# fmt: off
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as font_manager
import os
if os.environ.get("HELVETICA_MPL"):
    curdir = os.path.dirname(os.path.abspath(__file__))
    print(curdir)
    fontprop_reg = font_manager.FontProperties(fname="{}/Helvetica/Regular.ttf".format(curdir))
    fontprop_atl = font_manager.FontProperties(fname="{}/Helvetica/Bold_Italic.ttf".format(curdir))
    matplotlib.rcParams["font.family"] = fontprop_reg.get_name()
    print(fontprop_reg.get_name())
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams["axes.labelsize"] = 14
matplotlib.rcParams["font.size"] = 12
matplotlib.rcParams["xtick.top"] = True
matplotlib.rcParams["ytick.right"] = True
matplotlib.rcParams["xtick.direction"] = "in"
matplotlib.rcParams["ytick.direction"] = "in"
matplotlib.rcParams["xtick.labelsize"] = 12
matplotlib.rcParams["ytick.labelsize"] = 12
matplotlib.rcParams["xtick.minor.visible"] = True
matplotlib.rcParams["ytick.minor.visible"] = True
matplotlib.rcParams["xtick.major.width"] = 0.8
matplotlib.rcParams["xtick.minor.width"] = 0.8
matplotlib.rcParams["xtick.major.size"] = 7.0
matplotlib.rcParams["xtick.minor.size"] = 4.0
matplotlib.rcParams["xtick.major.pad"] = 1.5
matplotlib.rcParams["xtick.minor.pad"] = 1.4
matplotlib.rcParams["ytick.major.width"] = 0.8
matplotlib.rcParams["ytick.minor.width"] = 0.8
matplotlib.rcParams["ytick.major.size"] = 7.0
matplotlib.rcParams["ytick.minor.size"] = 4.0
matplotlib.rcParams["ytick.major.pad"] = 1.5
matplotlib.rcParams["ytick.minor.pad"] = 1.4
matplotlib.rcParams["legend.frameon"] = False
matplotlib.rcParams["legend.numpoints"] = 1
matplotlib.rcParams["legend.fontsize"] = 11
matplotlib.rcParams["legend.handlelength"] = 1.5
matplotlib.rcParams["axes.formatter.limits"] = [-4, 4]
matplotlib.rcParams["axes.formatter.use_mathtext"] = True
# fmt: on

import sys

if int(sys.version_info.major) < 3 or int(sys.version_info.minor) < 7:
    print ("require Python 3.7+")
    exit(1)
from dataclasses import dataclass
from typing import Optional, List
from pathlib import PosixPath
import yaml
import argparse
import uproot
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Sample:
    name: str
    signature: str
    color: str
    tex: str


class Histogram:
    def __init__(self, hfile, region, sample):
        self.hfile = hfile
        self.region = region
        self.sample = sample
        self.unit = ""
        self.mpl_title = ""
        try:
            self.uproothist = uproot.open(hfile).get(f"{self.region}_{self.sample.signature}")
            self.content = self.uproothist.values
            self.content[self.content < 0] = 1.0e-6
        except KeyError:
            self.uproothist = None
            self.content = None

    def __repr__(self):
        return f"<Histogram({self.hfile}, {self.region}, {self.sample})>"

    def __bool__(self):
        return self.uproothist is not None

    def __call__(self):
        return self.uproothist

    @property
    def sumw2(self):
        return self.uproothist.variances

    @property
    def error(self):
        return np.sqrt(self.sumw2)

    @property
    def bins(self):
        return self.uproothist.edges

    @property
    def bin_centers(self):
        return (self.bins[1:] + self.bins[:-1]) * 0.5

    @property
    def bin_width(self):
        return round(self.bins[-1] - self.bins[-2], 2)

    def has_uniform_bins(self):
        diffs = np.ediff1d(self.bins)
        return np.allclose(diffs, diffs[0])


def draw_ratio_with_line(ax, data, mc_sum, mc_err, yline=1.0, autoxscale=True):
    x1 = data.bins[0]
    x2 = data.bins[-1]
    err = np.sqrt(
        data.content / (mc_sum ** 2) + np.power(data.content * mc_err / (mc_sum ** 2), 2)
    )
    ax.plot([x1, x2], [yline, yline], color="gray", linestyle="solid", marker=None)
    ax.errorbar(data.bin_centers, data.content / mc_sum, yerr=err, fmt="ko", zorder=999)
    ax.set_ylabel("Data / MC")
    if autoxscale:
        ax.autoscale(enable=True, axis="x", tight=True)


def draw_atlas_label(ax, internal=True, extra_lines=[], x=0.050, y=0.905, s1=14, s2=12):
    # ax.text(x, y, "ATLAS", fontproperties=fontprop_atl, transform=ax.transAxes, size=s1)
    ax.text(x, y, "ATLAS", fontstyle="italic", fontweight="bold", transform=ax.transAxes, size=s1)
    if internal:
        ax.text(x + 0.15, y, r"Internal", transform=ax.transAxes, size=s1)
    for i, exline in enumerate(extra_lines):
        ax.text(x, y - (i + 1) * 0.06, exline, transform=ax.transAxes, size=s2)


def draw_labels(ax, histogram):
    if histogram.has_uniform_bins():
        ylabel_suffix = f" / {histogram.bin_width} {histogram.unit}"
    else:
        ylabel_suffix = f" / bin"
    ax.set_ylabel(f"Events{ylabel_suffix}", horizontalalignment="right", y=1.0)


def prefit_fig(args, region, data, histograms, band=None, figsize=(6, 5.25)):
    fig, (ax, axr) = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=figsize,
        gridspec_kw=dict(height_ratios=[3.25, 1], hspace=0.025),
    )
    expected_sum = np.sum([h.content for h in histograms], axis=0)
    expected_err = np.sqrt(np.sum([h.sumw2 for h in histograms], axis=0))
    ax.hist(
        [h.bin_centers for h in histograms],
        weights=[h.content for h in histograms],
        bins=histograms[0].bins,
        histtype="stepfilled",
        stacked=True,
        color=[h.sample.color for h in histograms],
        label=[h.sample.tex for h in histograms],
    )
    ax.errorbar(
        data.bin_centers, data.content, yerr=data.error, fmt="ko", label="Data", zorder=999
    )
    draw_labels(ax, histograms[0])
    ax.set_ylim([ax.get_ylim()[0], ax.get_ylim()[1] * 1.5])

    if band is not None:
        yerrlo = np.hstack([band.yerrorslow, band.yerrorslow[-1]])
        yerrhi = np.hstack([band.yerrorshigh, band.yerrorshigh[-1]])
        expected_sum4band = np.hstack([expected_sum, expected_sum[-1]])
        axr.fill_between(
            x=data.bins,
            y1=1 - yerrlo / expected_sum4band,
            y2=1 + yerrhi / expected_sum4band,
            step="post",
            hatch="///",
            facecolor="none",
            edgecolor="cornflowerblue",
            linewidth=0.0,
            zorder=99,
            label="Uncertainty",
        )
        ax.fill_between(
            x=data.bins,
            y1=(expected_sum4band - yerrlo),
            y2=(expected_sum4band + yerrhi),
            step="post",
            hatch="///",
            facecolor="none",
            edgecolor="cornflowerblue",
            linewidth=0.0,
            zorder=99,
            label="Uncertainty",
        )

    draw_ratio_with_line(axr, data, expected_sum, expected_err)
    axr.set_ylim([0.8, 1.2])
    axr.set_yticks([0.9, 1.0, 1.1])
    axr.set_xlabel(histograms[0].mpl_title, horizontalalignment="right", x=1.0)

    ax.legend(loc="upper right")
    handles, labels = ax.get_legend_handles_labels()
    handles.insert(0, handles.pop())
    labels.insert(0, labels.pop())
    ax.legend(handles, labels, loc="upper right")

    raw_region = region.split("reg")[-1].split("_")[0]
    extra_line1 = f"$\\sqrt{{s}}$ = 13 TeV, {args.lumi} fb$^{{-1}}$"
    extra_line2 = f"$pp\\rightarrow tW \\rightarrow e^{{\\pm}}\\mu^{{\\mp}}+{raw_region}$"
    extra_line3 = "Pre-fit"
    draw_atlas_label(ax, extra_lines=[extra_line1, extra_line2, extra_line3])

    fig.subplots_adjust(left=0.115, bottom=0.115, right=0.965, top=0.95)
    return fig, (ax, axr)


def prefit_histograms(args, region, samples):
    hfile = f"{args.workspace}/Histograms/{fit_name}_{region}_histos.root"
    bfile = f"{args.workspace}/Histograms/{fit_name}_{region}_preFit.root"
    band = uproot.open(bfile).get("g_totErr")
    histograms = [Histogram(hfile, region, sample) for sample in samples]
    data = Histogram(hfile, region, Sample("Data", "Data", "", "Data"))
    return data, histograms, band


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str, help="TRExFitter workspace")
    parser.add_argument("config", type=str, help="wt-stat configuration file")
    parser.add_argument("regions", type=str, nargs="+", help="Regions to generate plots")
    parser.add_argument("--out-dir", type=str, help="output directory for plots")
    parser.add_argument("--lumi", type=str, default="139", help="Integrated lumi.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    with open(args.config, "r") as f:
        yaml_config = yaml.load(f, Loader=yaml.FullLoader)
    samples = [Sample(**d) for d in yaml_config["samples"]]
    samples.reverse()

    outd = "."
    if args.out_dir:
        outd = args.out_dir
        if outd != ".":
            PosixPath(args.out_dir).mkdir(parents=True, exist_ok=True)

    fit_name = PosixPath(args.workspace).stem
    for region in args.regions:
        data, histograms, band = prefit_histograms(args, region, samples)
        fig, (ax, axr) = prefit_fig(args, region, data, histograms, band=band)
        fig.savefig(f"{outd}/{region}_preFit.pdf")
