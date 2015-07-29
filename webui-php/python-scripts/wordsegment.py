#""" code for image word segmenter """"

import cv2
import os, sys
from array import array
import preprocessing
import numpy as np
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
		       help = "Path to the directory that contains image file")

ap.add_argument("-b", "--book", required = True,
		help = "give a json file name to store the segmented result(ex:->filename.json)")


args = vars(ap.parse_args())
imagefile = args["image"]
segbookfilename = args['book']

bookdir_segresult="visual-search/segmented-books/"

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 
img = cv2.imread(imagefile,0)
#cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = preprocessing.binary_img(img)

sobelx = cv2.Sobel(binary,cv2.CV_64F,1,0,ksize=5)
#cv2.imshow('sobel',sobelx)

abs_sobel64f = np.absolute(sobelx)
sobel_8u = np.uint8(abs_sobel64f)
    
dilate_sobel = cv2.dilate(sobel_8u,kernel2,iterations = 1)
#cv2.imshow('dilate sobel',dilate_sobel)

opening = cv2.morphologyEx(dilate_sobel, cv2.MORPH_OPEN, kernel1)
#cv2.imshow('open sobel',opening)

dilation = cv2.dilate(binary,kernel2,iterations = 1)
erosion = cv2.dilate(dilation,kernel2,iterations = 1)

#cv2.imshow('d',erosion)

"""
contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtemp0',words_temp)
    
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
cv2.imshow('Outputimg2',img)
"""

contours, hierarchy = cv2.findContours(dilate_sobel,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
#cv2.imshow('Outputtemp0',words_temp)
    
words_temp = cv2.dilate(words_temp,kernel1,iterations = 1)
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

imagename=os.path.basename( imagefile)
splitimagename=imagename.split(".")
resultimagename=splitimagename[0]+"-result.jpg"

f= open(bookdir_segresult+segbookfilename,'w')
nMatches=0
str2="\n{\n    \"imagepath\": "+"\""+bookdir_segresult+"\""+","
f.write(str2) 
str3= "\n    \"segments\":[\n"
f.write(str3)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    if(nMatches != 0):
       f.write(",")
    str4 = "\n\t{"+"     \"geometry\":"+"{"+"\"x\":"+str(x)+","+"\"y\":"+str(y)+","+"\"width\":"+str((x+w)-x)+","+"\"height\":"+str((y+h)-y)+ "}"+"}"
    f.write(str4)
    nMatches = nMatches+1
str5="\n]\n}\n"
f.write(str5)
f.close()
      
#cv2.imshow('Outputimg2',img)
cv2.imwrite("visual-search/segmented-images/"+resultimagename,img)       
cv2.waitKey(0)
cv2.destroyAllWindows()
print bookdir_segresult+segbookfilename


