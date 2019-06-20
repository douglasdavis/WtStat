"""
This is a script which reads in two different TRExFitter fit
directories to plot the pulls on top of eachother. It requires
matplotlib.
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np

class NuisPar(object):
    def __init__(self, name, mean, sigma):
        self.name = name
        self.mean = mean
        self.sigma = sigma

parser = argparse.ArgumentParser()
parser.add_argument("fit1", type=str, help="first fit")
parser.add_argument("fit2", type=str, help="second fit")
parser.add_argument("--titles", type=str, nargs=2, help="legend titles", default=["fit1", "fit2"])
parser.add_argument("--prefixes", type=str, nargs="+", help="prefixes of uncertainties to show", default=[])
parser.add_argument("--out", type=str, required=True, help="output file")
parser.add_argument("--just-one", action="store_true", help="only plot one")
args = parser.parse_args()

startswith_test = tuple(args.prefixes)

fit1, fit2 = [], []
fit1_resunc = [0, 0]
fit2_resunc = [0, 0]

with open("{}/tW/Fits/tW.txt".format(args.fit1)) as f:
    for line in f.readlines():
        if line.startswith(startswith_test):
            try:
                name, mean, sigma, _ = tuple(line.split())
            except ValueError:
                continue
            fit1.append(NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma)))
        elif line.startswith("SigXsec"):
            fit1_resunc[0] = round(float(line.split()[2]), 3)
        elif line.startswith("mu_ttbar"):
            fit1_resunc[1] = round(float(line.split()[2]), 3)
with open("{}/tW/Fits/tW.txt".format(args.fit2)) as f:
    for line in f.readlines():
        if line.startswith(startswith_test):
            try:
                name, mean, sigma, _ = tuple(line.split())
            except ValueError:
                continue
            fit2.append(NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma)))
        elif line.startswith("SigXsec"):
            fit2_resunc[0] = round(float(line.split()[2]), 3)
        elif line.startswith("mu_ttbar"):
            fit2_resunc[1] = round(float(line.split()[2]), 3)


title1, title2 = args.titles
title1 = "{} ({}, {})".format(title1, fit1_resunc[0], fit1_resunc[1])
title2 = "{} ({}, {})".format(title2, fit2_resunc[0], fit2_resunc[1])
yval, ylabels, xerr1, xerr2 = [], [], [], []

i = 0
for alpha1 in fit1:
    for alpha2 in fit2:
        if alpha1.name == alpha2.name and alpha1.name not in ylabels:
            name = alpha1.name
            name = name.replace("ttbar", r"$t\bar{t}$").replace("tW", r"$tW$").replace(" PS", " Parton Shower")
            name = name.replace(" HS", " NLO matching/Hard Scatter").replace(" AR", " Add. Rad.")
            name = name.replace(" DRDS", " DR vs DS")
            ylabels.append(name)
            yval.append(i + 1)
            xerr1.append(alpha1.sigma)
            xerr2.append(alpha2.sigma)
            i = i + 1


Y_OFFSET_PT = 0.09
Y_OFFSET_TEXT = 0.05
X_OFFSET_TEXT = 0.035

if args.just_one:
    Y_OFFSET_PT = 0

fig, ax = plt.subplots(figsize=(10, len(yval)*.5))
ax.fill_betweenx([-50, 500], -2, 2, color="yellow")
ax.fill_betweenx([-50, 500], -1, 1, color="limegreen")
ax.set_yticks(yval)
ax.set_yticklabels(ylabels)
ax.errorbar(np.zeros_like(yval), np.array(yval) + Y_OFFSET_PT, xerr=xerr1, label=title1, fmt="ko", capsize=5 if args.just_one else 2)
if not args.just_one:
    ax.errorbar(np.zeros_like(yval), np.array(yval) - Y_OFFSET_PT, xerr=xerr2, label=title2, fmt="ro", capsize=2)
for f1e, f2e, iyval in zip(xerr1, xerr2, yval):
    ax.text(f1e + X_OFFSET_TEXT, iyval + Y_OFFSET_TEXT, "{}".format(round(f1e,3)), color="black")
    if not args.just_one:
        ax.text(-f2e - X_OFFSET_TEXT, iyval - Y_OFFSET_TEXT, "{}".format(round(f2e,3)), color="red", horizontalalignment="right", verticalalignment="top")
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([ 0.0, len(yval)+1])
ax.set_xlabel(r"$\left(\hat\theta - \theta_0\right) / \Delta \theta$")
if not args.just_one:
    ax.legend(bbox_to_anchor=(0, 1.01, 1, .01), loc=3, ncol=2, borderaxespad=0, mode="expand")
ax.grid(color="black", alpha=0.15)
fig.subplots_adjust(left=0.4)
fig.savefig(args.out, bbox_inches="tight")
