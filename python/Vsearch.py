import os, sys
from array import array
import cv2
import numpy as np
import json
import argparse
import shutil
import searchalgo
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

	


#first commandline argument -: '{"img":"test.jpg" ,"coord":{"x":1,"y":2,"w":20,"h":30}}'
data = json.loads(sys.argv[1])
srcimg = json.dumps( data['img'])
tempimgcoord = json.dumps(data['coord'])

print srcimg
print tempimgcoord

#second commandline argument -: "template image(temp.jpg)" 
tempimg = sys.argv[2]

#third commandline argument -: "book.json(book.json contains images)"
book = str(sys.argv[3])



try:
    #4th argument -: "Enter Algorithm (flann or templatematch)" 
    algo = str(sys.argv[4])
    #if ( algo == "flannsearch"):
    print " algo:",algo
	#searchalgo.flannsearch()
    #elif (algo=="templatesearch"):
            #print "template algo" 
            #searchalgo.templatesearch()

except IndexError:
       algo = "templatematch"
       print "Template Match Algorithm Used"
       #searchalgo.templatesearch()

try:
   #5th argument -: "threshold value(0.6)"
    
    threshval = float(sys.argv[5])
    #if ( algo == "flannsearch"):
	 #print "flann algo"
         #searchalgo.flannsearch()
    #elif ( algo=="templatesearch"):
	  #print "template algo"
          #searchalgo.templatesearch()

except IndexError:
       threshval = 0.7
       print "Defalut Threshold value=0.7 Taken"
       #searchalgo.templatesearch()



if(algo=="flannsearch"):
   print "FLANN "
   searchalgo.flannsearch()

elif (algo=="templatesearch"):
    print "TEMPLATE"
    searchalgo.templatesearch(tempimg,book,threshval)

else: 
    print "DEFAULT"
    searchalgo.templatesearch()


#print os.path
#vsearch(tempimg,book,threshval,algo)









