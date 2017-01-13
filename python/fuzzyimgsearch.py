import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--json", required = True,
				       help = "Path to the directory that contains the books(json file)")

ap.add_argument("-i", "--tempimg", required = True,
				       help = "Path to template image")

ap.add_argument("-b", "--book", required = True,
				help = "give a json file name to store the segmented result(ex:->filename.json)")


args = vars(ap.parse_args())
jsonfile = args["json"]
tempimg = args["tempimg"]
segbookfilename = args['book']
fuzzysegbookdir = "visual-search/fuzzysegmented-books/"
searchedimages="visual-search/searched-images/"
#f= open(fuzzysegbookdir+segbookfilename,'w')

with open( jsonfile ) as f :
     d = json.load( f )
allimages = []
allimages = d['book']['images']
#nMatches = 0
#nMatches1=0
f= open(fuzzysegbookdir+segbookfilename,'w')
str2="\n{\n    \"imagepath\": "+"\""+fuzzysegbookdir+"\""+","
f.write(str2)
str3="\n    \"template-imagepath\": "+"\""+tempimg+  "\""+","
f.write(str3)
str4= "\n    \"segments\":[\n"
f.write(str4)

for i in range(len(allimages)):
    nMatches = 0
    nMatches1=0
    #str2="\n{\n    \"imagepath\": "+"\""+fuzzysegbookdir+"\""+","
    #f.write(str2)    
    #str3="\n    \"template-imagepath\": "+"\""+tempimg+ "\""+","
    #f.write(str3)
    #str4= "\n    \"segments\":[\n"
    #f.write(str4)
    
    img_rgb = cv2.imread( allimages[i])
    img_gray = cv2.cvtColor( img_rgb, cv2.COLOR_BGR2GRAY )
    templateimg=cv2.imread(tempimg,0)
    w, h = templateimg.shape[::-1]
    res = cv2.matchTemplate( img_gray, templateimg, cv2.TM_CCOEFF_NORMED )
    threshold = 0.7
    loc = np.where( res >= threshold )

    for pt in zip( *loc[::-1] ):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
       
	if(nMatches != 0):
	    f.write(",")
	str5="\n\t{"+"     \"geometry\":"+"{"+"\'x\':" +str(pt[0])+"\t"+"\'y\':"+str(pt[1])+"\t"+"\'width\':"+str(pt[0]+w)+"\t"+"\'height\':"+str(pt[1]+h)+"}"+" }"  
	f.write(str5)
        nMatches = nMatches+1
        #for i in range(10):
            #cv2.imwrite(str(i)+'.png',img_rgb)
    str6="\n]\n}\n"
    f.write(str6)
    str6="\n]\n}\n"
    f.write(str6)
    #f.close()
   
    #for i in range(10):
    cv2.imwrite(str(i)+'.png',img_rgb)


        
    #f.close() 
    cv2.waitKey(3000) 
    
