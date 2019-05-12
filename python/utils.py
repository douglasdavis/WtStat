import os
import subprocess
import time
import logging

log = logging.getLogger(__name__)


def parallel_subprocess(coms, max_tasks=8, logpref="log"):
    commands = coms[:]
    taskn, processes, total_todo, total_done = 0, [], len(commands), 0
    while True:
        while commands and len(processes) < max_tasks:
            task = commands.pop()
            stdoutname = "{}.{}.stdout".format(logpref, taskn)
            stderrname = "{}.{}.stderr".format(logpref, taskn)
            taskn += 1
            with open(stdoutname, "w") as sout, open(stderrname, "w") as serr:
                log.info("Starting {}".format(task))
                processes.append(
                    subprocess.Popen(task, shell=True, stdout=sout, stderr=serr)
                )

        for p in processes:
            if p.poll() is not None:
                if p.returncode == 0:
                    total_done += 1
                    log.info("{}/{} done".format(total_done, total_todo))
                    processes.remove(p)
                else:
                    log.warn("return code is {}".format(p.returncode))

        if not processes and not commands:
            break
        else:
            time.sleep(0.5)

    return 0


def hfilesplit(path):
    arg1 = "/".join(os.path.abspath(path).split("/")[:-1])
    arg2 = os.path.abspath(path).split("/")[-1].split(".root")[0]
    return '"{}"'.format(arg1), '"{}"'.format(arg2)
