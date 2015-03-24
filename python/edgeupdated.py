import cv2
import numpy as np
from matplotlib import pyplot as plt
import signal
import time

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
#interrupted = False

#def signal_handler(signum, frame):
    #print("W: custom interrupt handler called.")
    #cv2.destroyAllWindows()

#signal.signal(signal.SIGINT, signal_handler)
img = cv2.imread('2.jpg',0)
cv2.imshow("img",img)

blur=cv2.medianBlur(img,5)
cl1 = clahe.apply(blur)
#cv2.imshow('cl1', cl1)

circles_mask = cv2.dilate(cl1,kernel1,iterations = 6)
circles_mask = (255-circles_mask)
#cv2.imshow('circles_mask', circles_mask)

circles_mask = cv2.threshold(circles_mask, 0, 255, cv2.THRESH_BINARY)[1]
edges = cv2.Canny(cl1,100,200)

#edges = cv2.bitwise_and(edges,edges,mask=circles_mask) 
#cv2.imshow('edges', edges)
dilation = cv2.dilate(edges,kernel1,iterations = 1)
#cv2.imshow('dilation', dilation)

display = cv2.bitwise_and(img,img,mask=dilation) 
#cv2.imshow('display', display)
cl2 = clahe.apply(display)
cl2 = clahe.apply(cl2)



ret,th = cv2.threshold(cl2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th = 255 - th

thg = cv2.adaptiveThreshold(display,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

#cv2.imshow('thg', thg)

#cv2.imshow('th', th)


final = cv2.bitwise_and(dilation,dilation,mask=th) 
#cv2.imshow('final', final)
cv2.imwrite("final1.jpg",final)

finalg = cv2.bitwise_and(dilation,dilation,mask=thg) 
#cv2.imshow('finalg', finalg)
cv2.imwrite("final2.jpg",finalg)

finalg = 255 - finalg

abso = cv2.bitwise_and(dilation,dilation,mask=finalg) 
#cv2.imshow('abso', abso)
cv2.imwrite("final3.jpg",abso)

cv2.waitKey(0)








