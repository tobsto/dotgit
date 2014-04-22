#!/usr/bin/python
import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='Configure Git')
args = parser.parse_args()

def cont(s):
    cont=raw_input("%s - continue(Y/n)?" % s)
    if cont!="n":
        return True
    else:
        return False

def run(cmd):
        subprocess.call(cmd, shell=True)

# Installation:
if cont("Configure Git"):
    run("cp ~/.git/gitconfig ~/.gitconfig")
    run("cp ~/.git/git-completion.bash ~/.git-completion.bash")
