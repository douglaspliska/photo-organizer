import os
import sys
import shutil  # used to move images
from PIL import Image  # used to retrieve metadata from images
from PIL.ExifTags import TAGS
from os.path import expanduser  # used path to get current user information
from pathlib import Path

# get current user
home = expanduser("~")
user = home[9:]

# create source and destination
source = "/Users/" + user + "/Desktop/Source"
destination = "/Users/" + user + "/Desktop/Destination"

# switch statement to determine month
def monthName(month):
    switcher = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'August'
    }
    return switcher.get(month)

for subdir, dirs, files in os.walk(source):

    # loop through files in loop and create filepath with info
    for filename in files:
        filepath = subdir + os.sep + filename

        # if file is hidden, skip
        if filename.startswith("._"):
            continue

        # if file doesn't end with jpg, png, or jpeg...
        if not (filepath.endswith(".JPG") or filepath.endswith(".png") or filepath.endswith(".jpg") or filepath.endswith(".PNG") or filepath.endswith(".jpeg") or filepath.endswith(".JPEG")):
            continue

        # if file ends with jpg, png, or jpeg...
        if filepath.endswith(".jpg") or filepath.endswith(".png") or filepath.endswith(".JPG") or filepath.endswith(".PNG") or filepath.endswith(".jpeg") or filepath.endswith(".JPEG"):

            # open image
            img = Image.open(filepath)
            exif = {}

        try:
            # loop through tags and value properties of image
            for tag, value in img._getexif().items():
                if tag in TAGS:
                    exif[TAGS[tag]] = value
        except (KeyError, AttributeError, NameError):
            continue

        try:
            # create variable for dates then for year and month
            time = exif['DateTimeOriginal']
            year = time[:4]
            month = int(time[5:7])
        except (KeyError, AttributeError, NameError):
            continue

        try:
            # create new folder for year if not one already
            if os.path.isdir(destination + "/" + year) != True:
                os.mkdir(destination + "/" + year)
        except (KeyError, AttributeError, NameError):
            continue

        try:
            # use switch statement function create path for image
            path = destination + "/" + year + "/" + monthName(month)

            # move image to destination and, if none exist, create a new directory and move it there
            if os.path.isdir(path) == True:
                shutil.copy(filepath, path)
                img.close()
                os.remove(filepath)
            else:
                os.mkdir(path)
                shutil.copy(filepath, path)
                img.close()
                os.remove(filepath)
        except (KeyError, AttributeError, NameError):
            continue
            
        try:
            # print out messages showing source, destination, year, and month of file being transferred
            print('From:', source)
            print('To:', path)
            print('Year:', year)
            print('Month:', monthName(month))
        except (KeyError, AttributeError, NameError):
            continue

print("Finalizing...")
img.close()

# move leftover unsupported files and images to unsupported folder
for subdir, dirs, files in os.walk(source):

    # loop through files in loop and create filepath with info
    for filename in files:
        filepath = subdir + os.sep + filename
        destination = "/Users/" + user + "/Desktop/Destination/Unsupported"

        if os.path.isdir("/Users/" + user + "/Desktop/Destination/Unsupported") != True:
            os.mkdir("/Users/" + user + "/Desktop/Destination/Unsupported")

        dest = shutil.copy(filepath, destination)
        os.remove(filepath)