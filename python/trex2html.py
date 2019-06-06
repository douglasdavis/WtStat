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


def plots(doc, tag, text):
    with tag("h2"):
        text("Region Plots")
    with tag("div", klass="container"):
        for f in os.listdir("Plots"):
            if f == "Summary.png":
                continue
            doc.stag("img", src="./Plots/{}".format(f), klass="regimg")
        if os.path.exists("./Plots/Summary.png"):
            doc.stag("img", src="./Plots/Summary.png", klass="regimg")


def systematics(doc, tag, text):
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
                    doc.stag("img", src="./Systematics/{}/{}".format(sys, f), klass="sysimg")


def generate_html(directory):
    doc, tag, text = Doc().tagtext()

    doc.asis("<!DOCTYPE html>")

    with tag("html"):
        with tag("head"):
            with tag("style", type="text/css"):
                text(CSS)

        with tag("body"):
            plots(doc, tag, text)
            top_level(doc, tag, text)
            systematics(doc, tag, text)

    return indent(doc.getvalue())


def trex2html(directory):
    if not os.path.exists(directory):
        print ("workspace directory ({}) doesn't exist, exiting".format(directory))
        return 0
    curdir = os.getcwd()
    os.chdir(directory)
    text = generate_html(directory)
    os.chdir(curdir)
    with open("{}/index.html".format(directory), "w") as f:
        f.write(text)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str, help="TRExFitter workspace")
    args = parser.parse_args()
    trex2html(args.workspace)
