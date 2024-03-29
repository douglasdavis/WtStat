import sys
import argparse
import re
import pprint


def sort_for_nominal_tree(file_list):
    regexes = {
        "ttbar": re.compile("ttbar_410472_FS"),
        "ttbar_AFII": re.compile("ttbar_410472_AFII"),
        "ttbar_RU_AFII": re.compile("ttbar_410482_AFII"),
        "ttbar_H7_AFII": re.compile("ttbar_410558_AFII"),
        "ttbar_MCaNLO_AFII": re.compile("ttbar_410465_AFII"),
        "tW": re.compile("tW_DR_41064(8|9)_FS"),
        "tW_AFII": re.compile("tW_DR_41064(8|9)_AFII"),
        "tW_DS_FS": re.compile("tW_DS_41065(6|7)_FS"),
        "tW_H7_AFII": re.compile("tW_DR_41103(8|9)_AFII"),
        "tW_MCaNLO_AFII": re.compile("tW_412003_AFII"),
    }

    files = {"Data": [], "Diboson": [], "Zjets": [], "MCNP": [], "ttV": []}
    for title in regexes:
        files[title] = []

    for f in file_list:
        if "nominal" not in f:
            continue

        if "MCNP" in f:
            files["MCNP"].append(f)
        elif "Data" in f:
            files["Data"].append(f)
        elif "Zjets" in f:
            files["Zjets"].append(f)
        elif "Diboson" in f:
            files["Diboson"].append(f)
        elif "ttV" in f:
            files["ttV"].append(f)

        elif "nominal" in f:
            for k, v in regexes.items():
                if v.search(f):
                    files[k].append(f)

    return files


def sort_for_systematic_trees(file_list):
    re_tW_sys_FS = re.compile("(tW_DR_[0-9]{6}_FS_MC16(a|d|e)_)")
    re_tt_sys_FS = re.compile("(ttbar_[0-9]{6}_FS_MC16(a|d|e)_)")
    files = {}
    for f in file_list:
        if "nominal" in f:
            continue
        else:
            if "tW_DR" in f:
                if re_tW_sys_FS.search(f):
                    sys_tree_name = f.split(re_tW_sys_FS.search(f).group(0))[-1].split(
                        "."
                    )[0]
                    if ("tW", sys_tree_name) not in files:
                        files[("tW", sys_tree_name)] = [f]
                    else:
                        files[("tW", sys_tree_name)].append(f)
            elif "ttbar" in f:
                if re_tt_sys_FS.search(f):
                    sys_tree_name = f.split(re_tt_sys_FS.search(f).group(0))[-1].split(
                        "."
                    )[0]
                    if ("ttbar", sys_tree_name) not in files:
                        files[("ttbar", sys_tree_name)] = [f]
                    else:
                        files[("ttbar", sys_tree_name)].append(f)
    return files


def create_nominal_executions(
    sorted_files, tree_prefix="WtTMVA", outfile="histograms.root", sys_weights=False
):
    exe_list = []
    for title, files in sorted_files.items():
        if not files:
            continue
        spaced_files = "-i {}".format(" ".join(files))
        exe = "wt-stat-hist-gen -o {ofile} -t {tp} -s nominal -n {title} {files}".format(
            ofile=outfile, tp=tree_prefix, title=title, files=spaced_files
        )
        if sys_weights:
            if title == "tW" or title == "ttbar":
                exe = "{} -w".format(exe)

        if (
            "ttbar_RU" in title
            or title == "ttbar"
            or "ttbar_AFII" in title
            or title == "tW"
        ):
            exe = "{} -x weight_sys_radLo weight_sys_radHi".format(exe)

        exe_list.append(exe)

    return exe_list


def create_systtree_executions(
    sorted_files, tree_prefix="WtTMVA", outfile="histograms.root"
):
    exe_list = []
    for k, files in sorted_files.items():
        if not files:
            continue
        title = k[0]
        suff = k[1]
        spaced_files = "-i {}".format(" ".join(files))
        exe = "wt-stat-hist-gen -o {ofile} -t {tp} -s {suff} -n {title} {files}".format(
            ofile=outfile, tp=tree_prefix, suff=suff, title=title, files=spaced_files
        )
        exe_list.append(exe)
    return exe_list
