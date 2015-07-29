import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse
import splitintolines_matformat


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
		       help = "Path to the directory that contains image file")

ap.add_argument("-b", "--book", required = True,
		help = "give a json file name to store the segmented result(ex:->filename.json)")


ap.add_argument("-d", "--dir", required = True,
		help = "temporary directory")


args = vars(ap.parse_args())
imagefile = args["image"]
segbookfilename = args['book']
root_dir= args['dir']

image = root_dir+"/example-images/user_uploads/"+imagefile
#print image
#print image
#print imagefile;
#with open( jsonfile ) as f :
     #d = json.load( f )
#allimages = []
#allimages = d['book']['images']
#print allimages

def SplitIntoWords(docImg,segbookfilename,root_dir):
 
    splitintolines_matformat.SplitIntoLines(docImg)
   
    splitintolines_matformat.SplitLinesIntoWords(docImg)
   
    splitintolines_matformat.DisplayWordBoundaries(docImg,segbookfilename,root_dir)
    #print "hello"
     
         

#for i in range(len(allimages)):
    #print allimages[i]
    #SplitIntoWords(allimages[i],segbookfilename)

SplitIntoWords(image,segbookfilename,root_dir)

