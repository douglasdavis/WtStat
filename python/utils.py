import os

def hfilesplit(path):
    arg1 = "/".join(os.path.abspath(path).split("/")[:-1])
    arg2 = os.path.abspath(path).split("/")[-1].split(".root")[0]
    return '"{}"'.format(arg1), '"{}"'.format(arg2)
