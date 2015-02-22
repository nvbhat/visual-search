import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse
import splitintolines_matformat
#import splitintolines_updated

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--json", required = True,
		       help = "Path to the directory that contains the books(json file)")

ap.add_argument("-b", "--book", required = True,
		help = "give a json file name to store the segmented result(ex:->filename.json)")


args = vars(ap.parse_args())
jsonfile = args["json"]
segbookfilename = args['book']

with open( jsonfile ) as f :
     d = json.load( f )
allimages = []
allimages = d['book']['images']

def SplitIntoWords(docImg,segbookfilename):
     #print "hello"
     listimg = []
     listimg.append(docImg)
     for i in range(len(listimg)):
	 splitintolines_matformat.SplitIntoLines(listimg[i])
	 splitintolines_matformat.SplitLinesIntoWords(listimg[i])
         splitintolines_matformat.DisplayWordBoundaries(listimg[i],segbookfilename)
         

for i in range(0,len(allimages)):
    #print allimages[i]
    SplitIntoWords(allimages[i],segbookfilename)



