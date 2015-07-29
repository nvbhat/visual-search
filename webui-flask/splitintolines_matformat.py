import parameters
import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse
from vizdoc_config import *
#http://opencv.jp/opencv-2svn_org/py/cookbook.html

obj = parameters.Parameters()
def SplitIntoLines(img):		 
    print "image segmenter starts..."
    print img
    docImg =cv2.imread( img,cv2.CV_LOAD_IMAGE_GRAYSCALE )
    #cv2.imshow("image",docImg)
    #cv2.waitKey(2000)
   
    ret, otsu =cv2.threshold(docImg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    rows,cols = docImg.shape
    rowSums = []
    rowSum =0
    rowSums1 = []
    
    #print "Len:",rows,";","col-len:",cols
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
		 #print len(obj.m_lineBoundaries1)
	       	 p1=(0,lineTop)
		 p2=(cols-1,lineBottom)
		 cv2.rectangle(out3,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA,0)
		 
    print "first method worked"
    



def DisplayWordBoundaries(img,segbookfilename):
    
    #print "Segbookfile:",segbookfilename
    docImg =cv2.imread( img,cv2.CV_LOAD_IMAGE_GRAYSCALE )
    ret, m_docImage =cv2.threshold(docImg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    rows,cols = m_docImage.shape
    out3=cv.CreateImage((rows,cols),cv.CV_8UC3,1)  
    channels =[]
    channels.append(m_docImage)
    channels.append(m_docImage)
    channels.append(m_docImage)
    out3=cv2.merge(channels)
    splitsegbookfname=segbookfilename.split(".json")
    segimgname=splitsegbookfname[0]+".jpg"
    bookdir= "static/segments/"
    f= open(bookdir+segbookfilename,'w')
    
    #print segimgname
    #resultimg=str(img)
    #resultimgname=resultimg.split("/")
    #print resultimgname[2]
#    imageloc="http://
    str1=  "\n{\n    \"imagepath\": "+"\""+bookdir+"\""+"," 
    f.write(str1)
    str2="\n    \"imagelocation\": "+"\"http://127.0.0.1:5000/"+img+"\""+","
    f.write(str2) 
    str3= "\n    \"segments\":[\n"
    f.write(str3)
    wordBVec1 = []
    wordBVec2 = []
    lineB= [ ]
    lineB1= []
    lineB2 = []
    wordB= []
    wordB1 = []
    wordB2 = []
    
    #print obj.m_wordBoundaries[0],";",obj.m_wordBoundaries[2]
    for i in range(len(obj.m_wordBoundaries1)):
	if(i>0):
	       f.write(",")
	str4 = "\n\t{"+"     \"geometry\":"+"{"+"\"x\":"+str(obj.m_wordBoundaries1[i])+",\t"+"\"y\":"+str(obj.m_lineBoundaries_y[i])+",\t"+"\"height\":"+str(obj.m_wordBoundaries2[i]-obj.m_wordBoundaries1[i])+",\t"+"\"width\":"+str(obj.m_lineBoundaries_w[i]-obj.m_lineBoundaries_y[i])+ "}"+"}"
	f.write(str4)
	       
        p1 = (obj.m_wordBoundaries1[i],obj.m_lineBoundaries_y[i])
        p2 =(obj.m_wordBoundaries2[i],obj.m_lineBoundaries_w[i])
        cv2.rectangle(out3,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA,0)
   
    print "DONE"
    str5="\n]\n}\n"
    f.write(str5)
    cv2.imwrite("static/segmented-images/"+segimgname,out3)
    f.close()
    #cv2.imshow("result",out3)
    #cv2.waitKey()
    print "static/segmented-images/"+segimgname
    obj.segimgname="static/segmented-images/"+segimgname
      
    
def SplitLine(m_lineImage,wordBoundaries1 ,wordBoundaries2):
    
    col_sums = []
    col_sums1 = []
    col_sums = m_lineImage.cols
    #print "col sums",col_sums
    col_Sum=0
    for col in range(m_lineImage.cols):
        col_Sum=0
        for row in range(m_lineImage.rows):
            col_Sum += m_lineImage[row,col]
    
        col_sums = col_Sum/255
        for i in np.nditer(col_sums):
	    col_sums1.append(i)
   

    
    obj.m_white_row_threshold =(m_lineImage.rows) * obj.m_white_col_fill_factor
    lineLeft=0
    lineRight=0
    WordBoundariesTemp1 = []
    WordBoundariesTemp2 = []

    out3 = cv.CreateMat(m_lineImage.rows, m_lineImage.cols, cv.CV_8UC1)
    for i in range (len(col_sums1)):
	if( col_sums1[i-1] >=obj.m_white_row_threshold and col_sums1[i] <= obj.m_white_row_threshold ):
            lineLeft = i
	elif(col_sums1[i-1] <= obj.m_white_row_threshold and col_sums1[i] >=  obj.m_white_row_threshold ):
            lineRight = i
	    lineB = [lineLeft,lineRight]
            WordBoundariesTemp1.append(lineB[0])
	    WordBoundariesTemp2.append(lineB[1])
            p1=(lineLeft,0)
	    p2=(lineRight,m_lineImage.rows-1)
            cv.Rectangle(out3,p1,p2,cv.Scalar(255,0,255),1,cv.CV_AA,0)
            #cv.ShowImage("outimage",out3)
	    #cv.WaitKey(0)

    currId = 0
    wordBegin=0
    wordEnd=0
    wordBegin =WordBoundariesTemp1[0]
    #print "test:",wordBegin
    #print len(WordBoundariesTemp2)
    while ( currId < len(WordBoundariesTemp1)-1):
	   cwB = WordBoundariesTemp1[currId]
	   cwE = WordBoundariesTemp2[currId]
           nwB = WordBoundariesTemp1[currId+1]
	   nwE = WordBoundariesTemp2[currId+1]
	   gap = nwB - cwE + 1
           #print wordBegin
           if ( gap > obj.m_MIN_INTER_WORD_GAP ):
		   wordB = [wordBegin,cwE]
		  
		   
		   wordBoundaries1.append(wordB[0])
		   wordBoundaries2.append(wordB[1])
		   #print wordB[0]
                   wordBegin = nwB
		   #print wordBegin
	           	   
	   currId = currId +1
    
   

    wordB1 = WordBoundariesTemp1[len(WordBoundariesTemp1)-1]
    wordB2 = WordBoundariesTemp2[len(WordBoundariesTemp2)-1]
    #print wordB1,";",wordB2
    wordBoundaries1.append(wordB1)
    wordBoundaries2.append(wordB2)
    #obj.m_wordBoundaries=[wordB1,wordB2,obj.m_lineBoundaries1,obj.m_lineBoundaries2]
    


#Second method ---"SplitLinesIntoWords(image)" starts ---
def SplitLinesIntoWords(img):
    print "inside 2nd method..."
    print "split into words:",img
    

    greyimg = cv.LoadImageM(img, cv.CV_LOAD_IMAGE_GRAYSCALE)
    m_docImage = cv.CreateMat(greyimg.rows, greyimg.cols, cv.CV_8UC1)
    cv.Threshold(greyimg,m_docImage,0,255,cv.CV_THRESH_OTSU);
    m_lineImage = cv.CreateMat(greyimg.height, greyimg.width, cv.CV_8UC1)
   

    #print len(obj.m_lineBoundaries1)
    for i in range(0,len(obj.m_lineBoundaries1)):
	#print obj.m_lineBoundaries1[i]
	currLineTop =obj.m_lineBoundaries1[i]
        currLineBottom=obj.m_lineBoundaries2[i]    
        #print currLineTop,";",currLineBottom
        p1=(0,currLineTop)
        p2=(greyimg.cols,currLineBottom)

        m_lineImage = cv.GetSubRect(m_docImage,(0,currLineTop,m_docImage.cols,currLineBottom-currLineTop+1))
        cv.SaveImage("lineImage.jpg",m_lineImage)
	wordBoundaries1 = []
	wordBoundaries2 = []

        SplitLine(m_lineImage,wordBoundaries1,wordBoundaries2)

        for k in range(len(wordBoundaries1)):
	    obj.m_wordBoundaries1.append(wordBoundaries1[k])
            obj.m_wordBoundaries2.append(wordBoundaries2[k])
	    obj.m_lineBoundaries_y.append(obj.m_lineBoundaries1[i])
	    obj.m_lineBoundaries_w.append(obj.m_lineBoundaries2[i])
       
      
    
    
  

