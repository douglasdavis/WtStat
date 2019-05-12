import os
import re

def files_from_dir(ntdir, regstr):
    retest = re.compile(regstr)
    flist = os.listdir(ntdir)
    files = set()
    for f in flist:
        if retest.match(f):
            files.add(f[:-5].replace("_nominal.bdt_response", ""))
    return ",".join(files)


def generic_region(name, sbtype, sel, var, nbins, xmin, xmax, vtitle, label, zs=None, zb=None, rebin=None):
    bk = r"""
Region: {0}
  Type: {1}
  Selection: "{2}"
  Variable: "{3}",{4},{5},{6}
  VariableTitle: "{7}"
  Label: {8}
  ShortLabel: {8}""".format(name, sbtype, sel, var, nbins, xmin, xmax, vtitle, label)
    if zs is not None and zb is not None:
        autobin = '"AutoBin","TransfoD",{},{}'.format(zs, zb)
        bk = "{}\n  Binning: {}\n".format(bk, autobin)
    elif rebin is not None:
        bk = "{}\n  Rebin: {}\n".format(bk, rebin)
    else:
        bk = "{}\n".format(bk)
    return bk
