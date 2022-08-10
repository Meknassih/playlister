import subprocess
import os
from time import sleep

dir_path = os.path.dirname(os.path.realpath(__file__))


def createPlaylist(url, name=""):
    print(url)
    # sleep(2)
    # print("done")
    # return 0
    proc = subprocess.run(
        ["spotdl", url], capture_output=True, text=True, cwd=dir_path)
    print(proc.stdout)

    return proc.stdout
