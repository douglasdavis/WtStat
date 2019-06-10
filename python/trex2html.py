#!/usr/bin/env python

from __future__ import print_function
import os
from WtStat.yattag import Doc, indent
from WtStat._css import CSS

def top_level(doc, tag, text):
    with tag("h2"):
        text("High Level Information")
    doc.stag("img", src="./NormFactors.png", klass="centerimg")
    doc.stag("img", src="./NuisPar.png", klass="centerimg")
    doc.stag("img", src="./Pruning.png", klass="centerimg")
    doc.stag("img", src="./CorrMatrix.png", klass="corrmatrix")
    doc.stag("img", src="./Gammas.png", klass="centerimg", alt="Gammas")
    if os.path.exists("./RankingSysts.png"):
        doc.stag("img", src="./RankingSysts.png", klass="centerimg", alt="Ranking")


def plots(doc, tag, text, regions):
    with tag("h2"):
        text("Region Plots")
    with tag("div", klass="container"):
        for f in os.listdir("Plots"):
            freg = f.split(".")[0]
            if f == "Summary.png":
                continue
            if freg not in regions:
                continue
            doc.stag("img", src="./Plots/{}".format(f), klass="regimg")
        if os.path.exists("./Plots/Summary.png"):
            doc.stag("img", src="./Plots/Summary.png", klass="regimg")


def systematics(doc, tag, text, regions):
    with tag("h2"):
        text("Systematics")
    sys_names = []
    for sys in os.listdir("Systematics"):
        sys_names.append(sys)
    sys_names.sort()
    for sys in sys_names:
        with tag("h3"):
            text(sys)
        with tag("div", klass="container"):
            for f in os.listdir("Systematics/{}".format(sys)):
                if ".png" in f:
                    freg = f.split("_")[0]
                    if freg not in regions:
                        continue
                    doc.stag("img", src="./Systematics/{}/{}".format(sys, f), klass="sysimg")


def generate_html(directory, regions):
    doc, tag, text = Doc().tagtext()

    doc.asis("<!DOCTYPE html>")

    with tag("html"):
        with tag("head"):
            with tag("style", type="text/css"):
                text(CSS)

        with tag("body"):
            plots(doc, tag, text, regions)
            top_level(doc, tag, text)
            systematics(doc, tag, text, regions)

    return indent(doc.getvalue())


def trex2html(args):
    if not os.path.exists(args.workspace):
        print ("workspace directory ({}) doesn't exist, exiting".format(args.workspace))
        return 0
    curdir = os.getcwd()
    os.chdir(args.workspace)
    text = generate_html(args.workspace, args.regions)
    os.chdir(curdir)
    with open("{}/index.html".format(args.workspace), "w") as f:
        f.write(text)
    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str, help="TRExFitter workspace")
    args = parser.parse_args()
    trex2html(args.workspace)
