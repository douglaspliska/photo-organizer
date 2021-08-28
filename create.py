import os
import sys
from os.path import expanduser
from pathlib import Path

# get current user
home = expanduser("~")
user = home[9:]

# create source and destination
source = "/Users/" + user + "/Desktop/Source"
destination = "/Users/" + user + "/Desktop/Destination"

# create source and destination folders
if os.path.isdir("/Users/" + user + "/Desktop/Source/") != True:
    os.mkdir("/Users/" + user + "/Desktop/Source/")

if os.path.isdir("/Users/" + user + "/Desktop/Destination/") != True:
    os.mkdir("/Users/" + user + "/Desktop/Destination/")
