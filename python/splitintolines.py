import parameters
import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse

obj = parameters.Parameters()

def SplitIntoLines(img):
    #print img
    docImg = cv2.imread( img,cv2.CV_LOAD_IMAGE_GRAYSCALE )
    #cv2.imshow("image",docImg)
    #cv2.waitKey(1000)
    ret, otsu =cv2.threshold(docImg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    rows,cols = docImg.shape
    rowSums = []
    rowSum =0
    rowSums1 = []
   
    for row in range(rows):
	rowSum =0;
	for col in range(cols):
            rowSum += otsu[row][col]
        rowSums=rowSum/255
	for i in np.nditer(rowSums):
            rowSums1.append(i)
    obj.m_white_row_threshold = cols * obj.m_white_row_fill_factor
    size = rows, cols,3
    out3=cv.CreateImage((rows,cols),cv.CV_8UC3,3) 
    channels =[]
    channels.append(otsu)
    channels.append(otsu)
    channels.append(otsu)
    out3=cv2.merge(channels)
  
    for i in range(1,len(rowSums1)):
	    if ( rowSums1[i-1] >= obj.m_white_row_threshold and rowSums1[i] <= obj.m_white_row_threshold ):
	       lineTop = i
            elif (rowSums1[i-1] <= obj.m_white_row_threshold and rowSums1[i] >=  obj.m_white_row_threshold ):
                 lineBottom = i
	         lineB = [lineTop,lineBottom]
		 
                 obj.m_lineBoundaries1.append(lineB[0])
                 obj.m_lineBoundaries2.append(lineB[1])
		 #obj.m_lineBoundaries +=(lineB[0],lineB[1])
                 #obj.m_lineBoundaries +=[lineB[0]]
	       	 p1=(0,lineTop)
		 p2=(cols-1,lineBottom)
		 cv2.rectangle(out3,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA,0)
		 #print lineB[0] 
    #cv2.imshow("img",otsu)
    #cv2.waitKey()
    #cv2.imwrite("lineimg.jpg",out3)
    
    print "first method worked"
    #a = array("i", [10],[20])
    #for value in a:
	#print(value)

#Second method ---"SplitLinesIntoWords(image)" starts ---
def SplitLinesIntoWords(img):
    print "inside 2nd method"
    
    #print obj.m_lineBoundaries[0:len(obj.m_lineBoundaries)]
   # for i in range(len(obj.m_lineBoundaries1)):
	 #for j in range(len(obj.m_lineBoundaries2)):
	#print obj.m_lineBoundaries1[i]
    currLineTop= obj.m_lineBoundaries1
    currLineBottom=obj.m_lineBoundaries2
    print currLineTop
    
    








    #alldata = []
    #alldata=[currLineBottomAll,currLineTopAll]
    alldata = {"currTop":currLineTop,"currBottom":currLineBottom}
    #keys = alldata.keys()
    #values = alldata.values()
    #print ("keys")
    #print (keys)
    
    #print values
    #print alldata["currTop"]
    top=[]
    top=alldata["currTop"]
    #print top
    bottom=[]
    bottom=alldata["currBottom"]

    #toplen=len(top)
    #bottomlen=len(bottom)
    
    arr = 0
    obj.m_lineBoundaries=top,bottom
    
    
   # print obj.m_lineBoundaries[0]
    #print obj.m_lineBoundaries[1]
    #for i in obj.m_lineBoundaries:
    #for i in range(len(obj.m_lineBoundaries[0])):
        #print obj.m_lineBoundaries[0][i]
	#arr +=obj.m_lineBoundaries[0][i]
    #print arr
    #for j in range(len(obj.m_lineBoundaries[1])):
	#print obj.m_lineBoundaries[1][j]

    #print obj.m_lineBoundaries
    #for t in top:
	#print t
    #for b in bottom:
        #print b
    #for i in alldata:
	#print alldata['currTop']
   # for i in range(len(currLineTopAll)):
	#obj.currLineTop = currLineTopAll[i]
        #print obj.currLineTop
	#print obj.currLineTop[i]
    #for i in range(len(currLineBottomAll)):
	#obj.currLineBottom = currLineBottomAll[i]
	#print obj.currLineBottom
   

    #print obj.m_lineBoundaries
    #print obj.m_lineBoundaries2
    #print len(obj.m_lineBoundaries1)


