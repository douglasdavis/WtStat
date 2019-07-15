"""
This is a script which reads in two different TRExFitter fit
directories to plot the pulls on top of eachother. It requires
matplotlib.
"""

import argparse
import matplotlib
matplotlib.rcParams["font.size"] = 16
matplotlib.rcParams["legend.frameon"] = False
matplotlib.rcParams["legend.fontsize"] = 15
matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np
import six

class NuisPar(object):
    def __init__(self, name, mean, sigma):
        self.name = name
        self.mean = mean
        self.sigma = sigma


def run(args, prefixes):
    Y_OFFSET_PT = 0.11
    Y_OFFSET_TEXT = 0.07
    X_OFFSET_TEXT = 0.035

    startswith_test = tuple(prefixes)

    fit1, fit2, fit3, fit4 = {}, {}, {}, {}
    fit1_resunc = [0, 0]
    fit2_resunc = [0, 0]
    fit3_resunc = [0, 0]
    fit4_resunc = [0, 0]

    with open("{0}/Fits/{0}.txt".format(args.fit1)) as f:
        for line in f.readlines():
            if line.startswith(startswith_test):
                try:
                    name, mean, sigma, _ = tuple(line.split())
                except ValueError:
                    continue
                fit1[name] = NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma))
            elif line.startswith("SigXsec"):
                fit1_resunc[0] = round(float(line.split()[2]), 3)
            elif line.startswith("mu_ttbar"):
                fit1_resunc[1] = round(float(line.split()[2]), 3)
    with open("{0}/Fits/{0}.txt".format(args.fit2)) as f:
        for line in f.readlines():
            if line.startswith(startswith_test):
                try:
                    name, mean, sigma, _ = tuple(line.split())
                except ValueError:
                    continue
                fit2[name] = NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma))
            elif line.startswith("SigXsec"):
                fit2_resunc[0] = round(float(line.split()[2]), 3)
            elif line.startswith("mu_ttbar"):
                fit2_resunc[1] = round(float(line.split()[2]), 3)
    with open("{0}/Fits/{0}.txt".format(args.fit3)) as f:
        for line in f.readlines():
            if line.startswith(startswith_test):
                try:
                    name, mean, sigma, _ = tuple(line.split())
                except ValueError:
                    continue
                fit3[name] = NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma))
            elif line.startswith("SigXsec"):
                fit3_resunc[0] = round(float(line.split()[2]), 3)
            elif line.startswith("mu_ttbar"):
                fit3_resunc[1] = round(float(line.split()[2]), 3)
    with open("{0}/Fits/{0}.txt".format(args.fit4)) as f:
        for line in f.readlines():
            if line.startswith(startswith_test):
                try:
                    name, mean, sigma, _ = tuple(line.split())
                except ValueError:
                    continue
                fit4[name] = NuisPar(name.replace("_", " "), min(abs(float(mean)), 0), float(sigma))
            elif line.startswith("SigXsec"):
                fit4_resunc[0] = round(float(line.split()[2]), 3)
            elif line.startswith("mu_ttbar"):
                fit4_resunc[1] = round(float(line.split()[2]), 3)

    title1, title2, title3, title4 = args.titles
    title1 = "{} ($\\Delta_{{tW}} = ${}, $\\Delta_{{t\\bar{{t}}}} = ${})".format(
        title1, fit1_resunc[0], fit1_resunc[1])
    title2 = "{} ($\\Delta_{{tW}} = ${}, $\\Delta_{{t\\bar{{t}}}} = ${})".format(
        title2, fit2_resunc[0], fit2_resunc[1])
    title3 = "{} ($\\Delta_{{tW}} = ${}, $\\Delta_{{t\\bar{{t}}}} = ${})".format(
        title3, fit3_resunc[0], fit3_resunc[1])
    title4 = "{} ($\\Delta_{{tW}} = ${}, $\\Delta_{{t\\bar{{t}}}} = ${})".format(
        title4, fit4_resunc[0], fit4_resunc[1])
    yval, ylabels, xerr1, xerr2, xerr3, xerr4 = [], [], [], [], [], []

    i = 0
    for alpha1key, alpha1 in six.iteritems(fit1):
        for alpha2key, alpha2 in six.iteritems(fit2):
            if alpha1.name == alpha2.name and alpha1.name not in ylabels:
                if alpha1key not in fit3:
                    continue
                if alpha1key not in fit4:
                    continue
                if alpha1key not in fit2:
                    continue
                name = alpha1.name
                name = name.replace("ttbar", r"$t\bar{t}$").replace("tW", r"$tW$").replace(" PS", " Parton Shower")
                name = name.replace(" HS", " NLO matching/Hard Scatter").replace(" AR", "")
                name = name.replace(" DRDS", " DR vs DS")
                ylabels.append(name)
                yval.append(i + 1)
                xerr1.append(alpha1.sigma)
                xerr2.append(alpha2.sigma)
                xerr3.append(fit3[alpha1key].sigma)
                xerr4.append(fit4[alpha1key].sigma)
                i = i + 1

    fig, ax = plt.subplots(figsize=(10, len(yval)*.6))
    ax.fill_betweenx([-50, 500], -2, 2, color="yellow")
    ax.fill_betweenx([-50, 500], -1, 1, color="limegreen")
    ax.set_yticks(yval)
    ax.set_yticklabels(ylabels)
    ax.errorbar(np.zeros_like(yval), np.array(yval) - 2*Y_OFFSET_PT,
                xerr=xerr1, label=title1, color="C0", marker="o", capsize=2, linestyle="")
    ax.errorbar(np.zeros_like(yval), np.array(yval) - Y_OFFSET_PT,
                xerr=xerr2, label=title2, color="C1", marker="o", capsize=2, linestyle="")
    ax.errorbar(np.zeros_like(yval), np.array(yval) + Y_OFFSET_PT,
                xerr=xerr3, label=title3, color="C3", marker="o", capsize=2, linestyle="")
    ax.errorbar(np.zeros_like(yval), np.array(yval) + 2*Y_OFFSET_PT,
                xerr=xerr4, label=title4, color="C4", marker="o", capsize=2, linestyle="")
    for f1e, f2e, f3e, f4e, iyval in zip(xerr1, xerr2, xerr3, xerr4, yval):
        ax.text(1 + X_OFFSET_TEXT, iyval - 3*Y_OFFSET_TEXT, "{}".format(round(f1e,3)), color="C0", size=12)
        ax.text(-1 - X_OFFSET_TEXT, iyval - 1.5*Y_OFFSET_TEXT, "{}".format(round(f2e,3)), color="C1", horizontalalignment="right", size=12)
        ax.text(1 + X_OFFSET_TEXT, iyval + 1.5*Y_OFFSET_TEXT, "{}".format(round(f3e,3)), color="C3", size=12)
        ax.text(-1 - X_OFFSET_TEXT, iyval + 3*Y_OFFSET_TEXT, "{}".format(round(f4e,3)), color="C4", horizontalalignment="right", size=12)
    ax.set_xlim([-1.75, 1.75])
    ax.set_ylim([ 0.0, len(yval)+1])
    ax.set_xlabel(r"$\left(\hat\theta - \theta_0\right) / \Delta \theta$")

    ax.legend(bbox_to_anchor=(0, 1.01, 1, .01), loc=3, ncol=1, borderaxespad=0, mode="expand")
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], bbox_to_anchor=(0, 1.01, 1, .01), loc=3, ncol=1, borderaxespad=0, mode="expand")
    ax.grid(color="black", alpha=0.15)
    fig.subplots_adjust(left=0.5)
    outfilepref = args.out.split(".pdf")[0]
    outfilename = "{}_{}.pdf".format(outfilepref, "_".join(prefixes))
    fig.savefig(outfilename, bbox_inches="tight")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fit1", type=str, help="first fit")
    parser.add_argument("fit2", type=str, help="second fit")
    parser.add_argument("fit3", type=str, help="third fit")
    parser.add_argument("fit4", type=str, help="fourth fit")
    parser.add_argument("--titles", type=str, nargs=4, help="legend titles", default=["fit1", "fit2", "fit3", "fit4"])
    parser.add_argument("--out", type=str, required=True, help="output file")
    args = parser.parse_args()

    prefix_sets = (["tW", "ttbar"],
                   ["B_ev"],
                   ["Jet_E", "Jet_F", "Jet_B", "Jet_P", "MET", "JVT", "Pileup"],
                   ["Norm", "Lumi"],
                   ["EG", "EL", "MU"],
                   ["PDF"],
                   ["Jet_JER"],
                   ["tW", "ttbar", "B_ev_B_0"])

    for pref in prefix_sets:
        run(args, pref)
