import os, sys
from array import array
import cv2
import numpy as np
import json
import argparse
import shutil

#usage:-> python imgsearchfinal.py "Templateimage" "book.json" "Threshold" "Algorithm for search" 

def vsearch(tempimg,book,threshval,algo):
    print tempimg
    print book
    print threshval
    print algo

    width, height = tempimg.shape[::-1]

    with open(book) as f :
	 bookdata=json.load( f )
    allimages = []
    allimages = bookdata['book']['images']
    print allimages

    for i in range(len(allimages)):
	print allimages[i]
	img_rgb = cv2.imread( allimages[i] )
	img_gray = cv2.cvtColor( img_rgb, cv2.COLOR_BGR2GRAY )
	#width, height = tempimg.shape[::-1]
	result = cv2.matchTemplate( img_gray, tempimg, cv2.TM_CCOEFF_NORMED )
	loc = np.where( result >= threshval )

	for pt in zip( *loc[::-1] ):
	    cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)
	cv2.imshow('result',img_rgb)
	cv2.waitKey(2000)    

	




tempimg = cv2.imread(sys.argv[1],0)
book = str(sys.argv[2])

try:
    threshval = float(sys.argv[3])
    
except IndexError:
       threshval = 0.7
       print "Defalut Threshold value=0.7 Taken"
       
try:
    algo = str(sys.argv[4])

except IndexError:
     algo = "Template-match"
     print "Template Match Algorithm Used"

#print os.path
vsearch(tempimg,book,threshval,algo)









