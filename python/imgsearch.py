import os, sys
from array import array
import cv2
import numpy as np
import json
  
print "visual search starts...."
#print "enter book images directory"
#bookimgdirpath = raw_input ()
#bookdirs = os.listdir(bookimgdirpath)

#infile = "../examples/book.json"
#infiledir ="../examples/" 

infile=sys.argv[1]
infiledir=sys.argv[2]

with open(infile) as f :
     d=json.load( f )

refimg = []
img = []
bookimgdata = []

#This would print all the files and directories
#for bookfilename in bookdirs:
   # print bookfilename
    #bookimgdata.append(bookfilename)
bookimgdirpath=d['book'] ['imagedirpath']
bookdirs=os.listdir(infiledir+bookimgdirpath)

f= open(infiledir+"/search/templatematch.json",'w')

for bookfilename in bookdirs:
    #print bookfilename
    bookimgdata.append(bookfilename)
    

#print "enter template images directory"
#tempimgdirpath = raw_input()
#tempdirs = os.listdir(tempimgdirpath)

tempimgdirpath = d[ 'page' ] [ 'templateimgpath' ]
tempdirs = os.listdir( infiledir+tempimgdirpath )

print "listing all template images"
for tempfilename in tempdirs:    
    print tempfilename

print "select a template image from the lists to search"
input_tempimg = raw_input()

#print "reading book images from:" + bookimgdirpath


for i in range(len(bookimgdata)):
    templateimg=cv2.imread(infiledir+tempimgdirpath+input_tempimg,0)
  
    print "   {\n "
    print "    \"imagepath\"",":\"",infiledir+bookimgdirpath,"\",","\n"
    print "    \"template-imagepath\"",":\"",infiledir+tempimgdirpath,"\",","\n"
    print "    \"segments\": ["

    str2="\n{\n    \"imagepath\": "+"\""+infiledir+bookimgdirpath+bookimgdata[i]+"\""+","
    f.write(str2)    
    str3="\n    \"template-imagepath\": "+"\""+infiledir+tempimgdirpath+input_tempimg+    "\""+","
    f.write(str3)
    str4= "\n    \"segments\":[\n"
    f.write(str4)

    nMatches = 0
    nMatches1=0
    img_rgb = cv2.imread( infiledir+bookimgdirpath+bookimgdata[i] )
    img_gray = cv2.cvtColor( img_rgb, cv2.COLOR_BGR2GRAY )
    w, h = templateimg.shape[::-1]
    res = cv2.matchTemplate( img_gray, templateimg, cv2.TM_CCOEFF_NORMED )
    threshold = 0.7
    loc = np.where( res >= threshold )
    
    
    for pt in zip( *loc[::-1] ):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        if(nMatches != 0):
          f.write(",") 
          print(",")
        print "\n    { 'geometry': {", "'x':", pt[0], "'y':", pt[1], "'width': ",pt[0] + w, "'height':", pt[1] + h, " } }"

        str5="\n\t{"+"     \"geometry\":"+"{"+"\'x\':" +str(pt[0])+"\t"+"\'y\':"+str(pt[1])+"\t"+"\'width\':"+str(pt[0]+w)+"\t"+"\'height\':"+str(pt[1]+h)+"}"+" }"  
        f.write(str5) 
        nMatches = nMatches+1
    print "\n]\n","}\n"
    #cv2.imshow('result',img_rgb)
    #cv2.waitKey(2000)    
    str6="\n]\n}\n"
    f.write(str6)
    


      
