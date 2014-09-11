import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
#import pygame
def SplitIntoLines(bookimgdirpath):
    img = cv2.imread( bookimgdirpath,cv2.CV_LOAD_IMAGE_GRAYSCALE )
    ret, otsu =cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite("binary-thresholded.png",otsu)
    
    m_white_row_threshold = 0
    m_white_row_fill_factor = 1.0
    m_white_col_threshold = 0
    m_white_col_fill_factor = 1.0
    m_MIN_INTER_WORD_GAP = 5
    
    m_lineBoundaries=[]
    m_lineBoundaries1=[]
    rows,cols = img.shape
    rowSums = []
    #rowSums = np.array([])
    rowSums = rows
    rowSum =0
    rowSums1 = []
    data = []
    #print rowSums1
    m_white_row_threshold=0 
    for row in range(rows):
        rowSum =0;
       
        for col in range(cols):
            rowSum += otsu[row][col]
            
        #print rowSum
        
        rowSums=rowSum/255
        #print rowSums
        for i in np.nditer(rowSums):
            #print i
            rowSums1.append(i)
    m_white_row_threshold = cols * m_white_row_fill_factor
    #print m_white_row_threshold 
    #out3 = cv2.zeros(rows,cols,cv2.CV_8UC3)
    size = rows, cols,3
    #out3 = np.zeros(size,dtype=cv2.uint8)
    out3=cv.CreateImage((rows,cols),cv.CV_8UC3,1)    
    #print rowSums
    channels =[]
    channels.append(otsu)
    channels.append(otsu)
    channels.append(otsu)
    out3=cv2.merge(channels)
    #cv2.imwrite('linerect.png',out3)
    lineTop=0
    lineBottom=0
    #lineB =[]
    arr = []
    for j in range (len(rowSums1)):
        #print "prev:",(rowSums1[j-1]),":","curr:",(rowSums1[j])
        if( rowSums1[j-1] >=m_white_row_threshold and rowSums1[j] <= m_white_row_threshold ):
            lineTop = j
        elif(rowSums1[j-1] <= m_white_row_threshold and rowSums1[j] >=  m_white_row_threshold ):
               lineBottom = j
               lineB = [lineTop,lineBottom]
               #data.append(lineTop)
               #data.append(lineBottom)
               #print lineB
               
               
               m_lineBoundaries.append(lineB[0])
               m_lineBoundaries1.append(lineB[1])
               #print m_lineBoundaries
               p1=(0,lineTop)
               p2=(cols-1,lineBottom)
               cv2.rectangle(out3,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA,0)
               SplitLinesIntoWords(otsu,lineB[0],lineB[1],cols,rows)                
    cv2.imwrite('result.png',out3)
   
    #print m_lineBoundaries
    #print lineB rowSums=rowSum/255
    #SplitLinesIntoWordsnew(otsu,m_lineBoundaries,m_lineBoundaries1,cols,rows)
    #SplitLinesIntoWords(otsu,m_lineBoundaries,m_lineBoundaries1,cols,rows) 
    
     
#def SplitLinesIntoWordsnew(img,m_lineBoundaries,m_lineBoundaries1,cols,rows): 
    #print m_lineBoundaries

    #for i in range(len(m_lineBoundaries)):
        
        #print m_lineBoundaries[i] 
   
            
    
    
    


    #cv2.imshow('result',img)
    #cv2.waitKey(2000)

def SplitLine(img,wordBoundaries,cols,rows):
    #cv2.imshow('img',img)
    #cv2.waitKey(0)
   
    col_sums = []
    col_sums1 = []
    col_sums = cols
    
    #col_sum = 0
    #for col in range(cols):
       # col_sum = 0
        #for row in range(rows):
            #col_sum += img[row][col]
            
        #col_sums = col_sum/255
        #print col_sums
        #for i in np.nditer( col_sums ):
            #col_sums1.append( i )
        #print col_sums1

        
def SplitLinesIntoWords(img,lineB1,lineB2,cols,rows):
    m_lineBoundaries=[lineB1,lineB2]

    currLineTop=lineB1
    currLineBottom=lineB2
    #print currLineTop
    #print m_lineBoundaries
    #currLineBoundaries=[][]
    #len1= len(m_lineBoundaries)
    #len2=len(m_lineBoundaries1)
    #m_lineB = m_lineBoundaries
    #print m_lineB
    #currLineTop1 =[]
    #currLineBottom1 = []
    #for i in range(len(m_lineBoundaries)):
        #currLineTop = m_lineBoundaries[i]
        #print "curlinetop:",currLineTop
        #currLineTop1.append(currLineTop)
    #print currLineTop1
    #for i in range(len(m_lineBoundaries)):
        #for j in range(len(m_lineBoundaries1)):
            #print m_lineBoundaries[i],";",m_lineBoundaries1[j]
            #currLineTop = m_lineBoundaries[i]
            #currLineBottom=m_lineBoundaries1[j]
            #print currLineBottom
     
    lineImg=cv.CreateImage((rows,cols),cv.CV_8UC3,1)
    channels =[]
    channels.append(img)
    channels.append(img)
    channels.append(img)
    lineImg=cv2.merge(channels)
    #cv2.rectangle(out3,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA,0)
    #cv2.rectangle(lineImg,0,currLineTop,cols,currLineBottom-currLineTop+1)
    #lineImg=cv2.rectangle(img,0,currLineTop,cols,currLineBottom-currLineTop+1)
    #print currLineTop,";",cols,";",currLineBottom-currLineTop+1
    p1=(0,currLineTop)
    p2=(cols,currLineBottom-currLineTop+1)

    cv2.rectangle(lineImg,p1,p2,cv.CV_RGB(255,0,255),1,cv.CV_AA)
    wordBoundaries = []
    SplitLine(lineImg,wordBoundaries,cols,rows)

    #cv2.imwrite('demo.png',lineImg)





def SplitIntoWords(bookimgdirpath,segmentedimgpath,outfile):
    #print bookimgdirpath,segmentedimgpath,outfile
    SplitIntoLines(bookimgdirpath)
    #SplitLinesIntoWords(bookimgdirpath);
    






print "initialized image Segementer..."
bookimgdata = []
with open('segment.json') as f :
     d=json.load( f )

bookimgdirpath=d['book'] ['imagedirpath']
bookdirs=os.listdir( bookimgdirpath)

for bookfilename in bookdirs:
        #print bookfilename
    bookimgdata.append(bookfilename)

segmentedimgpath=d['page'] ['segmentedimgpath']  
 
for i in range(len(bookimgdata)):
    #print bookimgdata[i]
    #print (bookimgdirpath+bookimgdata[i])
    SplitIntoWords(bookimgdirpath+bookimgdata[i],segmentedimgpath,"segmented_res"+bookimgdata[i])



   


















    
