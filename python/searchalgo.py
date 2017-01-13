import os, sys
from array import array
import cv2
import numpy as np
import json
import argparse
import shutil


def templatesearch(tempimg,book,threshval):
    print "template search starts.."
    print tempimg
    print book
    print threshval
    tempimg = cv2.imread(tempimg,0)
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
         result = cv2.matchTemplate( img_gray, tempimg, cv2.TM_CCOEFF_NORMED )
	 loc = np.where( result >= threshval )
         
	 for pt in zip( *loc[::-1] ):
             cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)
	 cv2.imshow('result',img_rgb)
	 cv2.waitKey(2000)




    

def flannsearch():
    print "flann search starts.."
