#!/usr/bin/python3

# -*- coding: utf-8 -*-

import os
import sys
from subprocess import check_call

if (sys.platform == "linux" or sys.platform == "linux2"):
    print("[*] Installation on Linux")
    print("[*] Start installation all requirements from the list:")
    print("[*] You must type your password")
    check_call(['sudo','pip3','install','-r','requirements.txt'])
ćŋ’
elif (sys.platform == "win32"):
    print("[*] Installation on Winsows")
    print("[*] Start installation all requirements from the list:")
    print("[*] You must type your password")
    #check_call(['pip3','install','-r','requirements.txt'])

    check_call(['pip3','install','-r','requirements.txt'])
    prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', 'NeedsAdminPrivilege.exe'],stdin=subprocess.PIPE)
    prog.stdin.write('password')
    prog.communicate()
