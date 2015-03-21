from __future__ import print_function
import glob
import os
os.chdir("/home/vtbhat/updates10001-v2/static/visual-search/segmented-books")
for file in glob.glob("*.json"):
    print(file)


