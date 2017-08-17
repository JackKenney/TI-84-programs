"""Converter from TI-84 .8Xp files to .txt files."""
# Author: Jack Kenney
# Date: 2017/08/17

# This program requires the installation of "basically-ti-basic"
# Which can be found at https://github.com/thenaterhood/basically-ti-basic
import os
from subprocess import call
# Determine which files to convert and move
names = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.8Xp'):
            names.append(file)
# Make sure the 8Xp directory has been created.
if not os.path.isdir("8Xp"):
    call(['mkdir', '8Xp'])
if not os.path.isdir("txt"):
    call(['mkdir', 'txt'])
# Begin
for name in names:
    txt = name[0:len(name)-4]+".txt"
    # Convert the files
    call(["basically-ti-basic", "-d", "-i", name, "-o", txt])
    # Move the source files into their directory
    call(["mv", name, "8Xp/"+name])
    # Move the txt files into their directory
    call(["mv", txt, "txt/"+txt])

# Sources for python scripting:
# https://docs.python.org/3/library/os.html#os.fwalk
# https://stackoverflow.com/questions/1274506/how-can-i-create-a-list-of-files-in-the-current-directory-and-its-subdirectories
# https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
