#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import pip
import subprocess
from subprocess import check_call

if (sys.platform == "linux" or sys.platform == "linux2"):
    print("[*] Installation on Linux")
    print("[*] Start installation all requirements from the list:")
    print("[*] You must type your password")
    check_call(['sudo','pip3','install','-r','requirements.txt'])

elif (sys.platform == "win32"):
    print("[*] Installation on Winsows")
    print("[*] Start installation all requirements from the list:")
    prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', 'winInstall.py'],stdin=subprocess.PIPE)
    prog.stdin.write("[*] You must type your password")
    prog.communicate()
