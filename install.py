#!/usr/bin/python3
# -*- coding: utf-8 -*-
import io
import os
import sys

import subprocess 
from subprocess import call

subprocess.call(['sudo','pip3','install','-r','requirements.txt'])

import pypandoc


"""
from distutils.core import setup
import py2exe

setup(console=['main.py'])