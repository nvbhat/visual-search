import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse

#Usage:-> python imgwordsegmenter.py  -j  /indexedbooks/Kandanu.json -b segoutput.json(give any file name to save the segmented result)

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--json", required = True,
	       help = "Path to the directory that contains the books(json file)")

ap.add_argument("-b", "--book", required = True,
	       help = "give segmented result file name json type(book.json)")



args = vars(ap.parse_args())
jsonfile = args["json"]
outputjsonfile = args["book"]


with open( jsonfile ) as f :
     d = json.load( f )
imgdirpath=d['book'] ['imagedirpath']

allimages = []
allimages = d['book']['images']



outfile = open ( "visual-search/segmented-books/"+outputjsonfile,'w' )
# Load the image
for i in range(0,len(allimages)):
    img = cv2.imread(allimages[i])
   
    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

   # smooth the image to avoid noises
    gray = cv2.medianBlur(gray,5)

    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
    thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

    # apply some dilation and erosion to join the gaps
    thresh = cv2.dilate(thresh,None,iterations = 3)
    thresh = cv2.erode(thresh,None,iterations = 2)

    # Find the contours
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    #write rect points to output json file
    str2="\n{\n    \"imagepath\": "+"\""+imgdirpath+"\""+","
    outfile.write(str2)
    str3= "\n    \"segments\":[\n"
    outfile.write(str3)
    nMatches = 0
    # For each contour, find the bounding rectangle and draw it
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)
         
	if ( nMatches != 0 ):
           outfile.write(",")
	   print (",")
	print ("\n\t{"+"     \"geometry\":"+"{"+"\'x\':" +str(x)+"\t"+"\'y\':"+str(y)+"\t"+"\'width\':"+str(x+w)+"\t"+"\'height\':"+str(y+h)+"}"+" }")
        str4="\n\t{"+"     \"geometry\":"+"{"+"\'x\':" +str(x)+"\t"+"\'y\':"+str(y)+"\t"+"\'width\':"+str(x+w)+"\t"+"\'height\':"+str(y+h)+"}"+" }"  
	outfile.write(str4) 
        nMatches = nMatches+1
     
    str5="\n]\n}\n"
    outfile.write(str5)

    #Finally show the image
    cv2.imshow('img',img)
    #cv2.imshow('res',thresh_color)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

    
