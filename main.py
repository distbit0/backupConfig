import shutil
import subprocess
import glob
import json
import os
import re
from shutil import copy2
from os import path

def getAbsPath(relPath):
    basepath = path.dirname(__file__)
    fullPath = path.abspath(path.join(basepath, relPath))

    return fullPath


def getConfig():
    configFileName = getAbsPath("./config.json")
    with open(configFileName) as config:
        config = json.loads(config.read())

    return config

def copy_and_rename_files(path_patterns):
    for path_pattern in path_patterns:
        pattern = getAbsPath("../" + path_pattern)
        print(pattern)
        for filePath in glob.glob(pattern, recursive=True):
            destFilePath = getAbsPath("../configFiles/" + filePath.replace("/", "-"))
            copy2(filePath, destFilePath)

if __name__ == "__main__":
    paths = getConfig()["backupPaths"]
    copy_and_rename_files(paths)
    os.system("/home/pimania/Dev/git-auto/git-auto -d " + getAbsPath("../configFiles/") + " -o -p")
