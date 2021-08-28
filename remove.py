import os
import sys
import shutil
from os.path import expanduser

# get current user
home = expanduser("~")
user = home[9:]

# create source and destination
source = "/Users/" + user + "/Desktop/Source"

# remove empty folders
shutil.rmtree(source)
