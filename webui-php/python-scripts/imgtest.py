import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse
import shutil

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
#print tempimg
bookdir="../../maindirectory/"
#print bookdir+jsonfile

basejsonfilename = os.path.basename( jsonfile)
splitbasejsonfname = basejsonfilename.split(".")
resultimages_dirname=splitbasejsonfname[0]

#code for creating folders to save result searched-images dynamically
#if folder is already exist it will override the contents inside the same folder.
storeresultimg_dir = r"../../visual-search/searched-images/"+resultimages_dirname
if not os.path.exists(storeresultimg_dir): 
   os.makedirs(storeresultimg_dir)
else:
    shutil.rmtree(storeresultimg_dir) #removes all the subdirectories!
    os.makedirs(storeresultimg_dir)

fuzzysegbookdir = "../../visual-search/fuzzysegmented-books/"
imagedir="../../example-images/";


with open( str(bookdir+jsonfile) ) as f :
     d = json.load( f )
allimages = []
allimages = d['book']['images']
#print allimages

f= open(fuzzysegbookdir+segbookfilename,'w')
"""str2="\n{\n    \"imagepath\": "+"\""+fuzzysegbookdir+"\""+","
f.write(str2)
str3="\n    \"template-imagepath\": "+"\""+tempimg+  "\""+","
f.write(str3)
str4= "\n    \"segments\":[\n"
f.write(str4)"""

for i in range(len(allimages)):
    nMatches = 0
    nMatches1=0
    str2="\n{\n    \"imagepath\": "+"\""+fuzzysegbookdir+"\""+","
    f.write(str2)    
    str3="\n    \"template-imagepath\": "+"\""+tempimg+ "\""+","
    f.write(str3)
    str4= "\n    \"segments\":[\n"
    f.write(str4)
    #print bookdir+allimages[i];
    splitimagename=allimages[i].split(".")
    resultimage=splitimagename[0]+"-result.jpg"
   
    #print resultimage;
    img_rgb = cv2.imread( imagedir+allimages[i])
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
    
    str6="\n]\n\n}\n"
    f.write(str6)
    
    #f.close()
    
    cv2.imwrite(storeresultimg_dir+"/"+resultimage,img_rgb)
    #cv2.imshow('result',img_rgb)
    cv2.waitKey(3000)  


