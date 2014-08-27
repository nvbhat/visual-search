import os, sys
from array import array
import cv2
import numpy as np
import json

print "visual search starts...."
#print "enter book images directory"
#bookimgdirpath = raw_input ()
#bookdirs = os.listdir(bookimgdirpath)

with open('book.json') as f :
     d=json.load( f )

refimg = []
img = []
bookimgdata = []

#This would print all the files and directories
#for bookfilename in bookdirs:
   # print bookfilename
    #bookimgdata.append(bookfilename)
bookimgdirpath=d['book'] ['imagedirpath']
bookdirs=os.listdir( bookimgdirpath)

for bookfilename in bookdirs:
    #print bookfilename
    bookimgdata.append(bookfilename)


#print "enter template images directory"
#tempimgdirpath = raw_input()
#tempdirs = os.listdir(tempimgdirpath)

tempimgdirpath = d[ 'page' ] [ 'templateimgpath' ]
tempdirs = os.listdir( tempimgdirpath )

print "listing all template images"
for tempfilename in tempdirs:    
    print tempfilename

print "select a template image from the lists to search"
input_tempimg = raw_input()

print "reading book images from:" + bookimgdirpath
#print bookimgdata

for i in range(len(bookimgdata)):
    print bookimgdata[i]
    #refimg = cv2.imread(bookimgdirpath+bookimgdata[i],0)
    #cv2.imshow('refimg', refimg[i])
    refimg.append(bookimgdirpath+bookimgdata[i])

for j in range(len(refimg)):
    print refimg[j]
    img_rgb=cv2.imread(refimg[j])
    img_gray=cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    templateimg=cv2.imread(tempimgdirpath+input_tempimg,0)
    w, h=templateimg.shape[::-1]

    res = cv2.matchTemplate( img_gray, templateimg, cv2.TM_CCOEFF_NORMED )
    threshold = 0.7
    loc = np.where( res >= threshold )
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    #cv2.imshow('refimg',refimg[j])
    #try:
    #img.append(cv2.imread(refimg[j]))
    cv2.imshow('result',img_rgb)
    cv2.waitKey(3000)
    #except IndexError:
           #pass
    #continue
#for k in range(len(img)):
    #cv2.imshow('ref',img[k])   
    #print img[k]
    #cv2.waitKey(2000)
         
