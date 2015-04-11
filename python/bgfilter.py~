import os,sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import signal
import time
import argparse

class bgfilter(object):
      def GenericFilter(self,infile,outfile):
	      #print infile,":",outfile
	      clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	      kernel1 = np.ones((5,5),np.uint8)
	      kernel2 = np.ones((3,3),np.uint8)
	      img = cv2.imread(str(infile),0)
	      cv2.imshow("img",img)
	      blur=cv2.medianBlur(img,5)
	      cl1 = clahe.apply(blur)
	      circles_mask = cv2.dilate(cl1,kernel1,iterations = 6)
	      circles_mask = (255-circles_mask)
	      circles_mask = cv2.threshold(circles_mask, 0, 255, cv2.THRESH_BINARY)[1]
	      edges = cv2.Canny(cl1,100,200)
	      dilation = cv2.dilate(edges,kernel1,iterations = 1)
	      display = cv2.bitwise_and(img,img,mask=dilation) 
	      cl2 = clahe.apply(display)
	      cl2 = clahe.apply(cl2)
	      ret,th = cv2.threshold(cl2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	      th = 255 - th
	      thg = cv2.adaptiveThreshold(display,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
			                  cv2.THRESH_BINARY,11,2)

	      saveimgfile=outfile.split(".")
	      print saveimgfile[1]

	      final = cv2.bitwise_and(dilation,dilation,mask=th) 
	      cv2.imwrite("Filtered-images/"+str(saveimgfile[0])+"1."+str(saveimgfile[1]),final)
	      finalg = cv2.bitwise_and(dilation,dilation,mask=thg) 
	      cv2.imwrite("Filtered-images/"+str(saveimgfile[0])+"2."+str(saveimgfile[1]),finalg)
	      finalg = 255 - finalg
	      abso = cv2.bitwise_and(dilation,dilation,mask=finalg) 
	      cv2.imwrite("Filtered-images/"+str(saveimgfile[0])+"orig."+str(saveimgfile[1]),abso)

	      cv2.waitKey(0)

      #def __init__ ( self,bgtype,infile,outfile ):
	  #self.bgtype=bgtype
	  #self.infile=infile
	  #self.outfile=outfile
	  #print bgtype
#bgfilterobj=bgfilter(None,None,None)
#print id(bgfilterobj)
      #def addFilterAlgo():
      #bgfilterobj=bgfilter(None,None,None)
      #print id(bgfilterobj)
#def getSupportedBGTypes():
    #return bgtype

