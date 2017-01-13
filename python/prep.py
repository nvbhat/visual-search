# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:09:51 2015

@author: suryo

Python module for preprocessing images of Indain manuscriptsfor further
processing and pattern matching.

This python module can perform the following functions:

1. Binarization - method binary_img(img) performs this function
2. Skew correction - method skew_correction(img) performs this function
"""

import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

"""
Method to binarize an image

Input: Grayscale image
Output: Binary image

The nature of the output is such that the text(foreground) has a colour 
value of (255,255,255), and the background has a value of (0,0,0).
"""
def binary_img(img):

    img_erode = cv2.dilate(img,kernel,iterations = 2)
    blur=cv2.medianBlur(img,5)

    mask1 = np.ones(img.shape[:2],np.uint8)
    """Applying histogram equalization"""
    cl1 = clahe.apply(blur)

    circles_mask = cv2.dilate(cl1,kernel,iterations = 1)
    circles_mask = (255-circles_mask)

    thresh = 1
    circles_mask = cv2.threshold(circles_mask, thresh, 255, cv2.THRESH_BINARY)[1]

    edges = cv2.Canny(cl1,100,200)

    edges = cv2.bitwise_and(edges,edges,mask=circles_mask) 

    dilation = cv2.dilate(edges,kernel,iterations = 1)

    display = cv2.bitwise_and(img,img,mask=dilation) 

    cl2 = clahe.apply(display)
    cl2 = clahe.apply(cl2)

    ret,th = cv2.threshold(cl2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th = 255 - th

    thg = cv2.adaptiveThreshold(display,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    final = cv2.bitwise_and(dilation,dilation,mask=th) 

    finalg = cv2.bitwise_and(dilation,dilation,mask=thg) 

    finalg = 255 - finalg
    
    abso = cv2.bitwise_and(dilation,dilation,mask=finalg) 
    
    return abso
    
"""
Method to correct the skew of an image

Input: Binary image
Output: Skew corrected binary image

The nature of the output is such that the binary image is rotated appropriately
to remove any angular skew.
"""
    
def skew_correction(img):
    areas = []  #stores all the areas of corresponding contours
    dev_areas = []  #stores all the areas of the contours within 1st std deviation in terms of area
    largest_white_pixels = [] #stores all the white pixels of the largest contour within 1st std deviation
    k = 0
    
    binary = binary_img(img)
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    upper_bound=len(contours)
    
    for c in contours:
        areas.append(cv2.contourArea(c))
        
    std_dev = np.std(areas)    
    for i in areas:
        dev_areas.append(i-std_dev)
        
    dev_contours = np.zeros(img.shape[:2],np.uint8)
    
    for i in dev_areas:
        if((i>(-std_dev)) and (i<=(std_dev))):
            cv2.drawContours(dev_contours, contours, k, (255,255,255), -1)
        k+=1
            
    sobely = cv2.Sobel(dev_contours,cv2.CV_64F,0,1,ksize=5)
    abs_sobel64f = np.absolute(sobely)
    sobel_8u = np.uint8(abs_sobel64f)
    
    largest_contour = np.zeros(img.shape[:2],np.uint8)
    
    """After the next step, we'll have the largest word in the image.
    Since all the words in different lines have to be parallel to each other,
    we'll take the largest word as the reference and find out it's alighment.
    We'll rotate the entire image accordingly"""
    
    contours, hierarchy = cv2.findContours(sobel_8u,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cv2.drawContours(largest_contour, contours, max_index, (255,255,255), -1)

    height, width = largest_contour.shape[:2]

    all_white_pixels = []

    for i in range(0,height):
        for j in range(0,width):
            if(largest_contour.item(i,j)==255):
                largest_white_pixels.append([i,j])
            

    matrix = np.array(largest_white_pixels)
    
    """Finding covariance matrix"""
    C = np.cov(matrix.T)

    eigenvalues, eigenvectors = np.linalg.eig(C)

    """Finding max eigenvalue"""
    max_ev = max(eigenvalues)
    """Finding index of max eigenvalue"""
    max_index =  eigenvalues.argmax(axis=0)

    """The largest eigen value gives the approximate length of the bounding
    ellipse around the largest word. If we follow the index of the largest 
    eigen value and find the eigen vectors in the column of that index,
    we'll get the x and y coordinates of it's centre."""
    y = eigenvectors[1,max_index]
    x = eigenvectors[0,max_index]

    angle = (np.arctan2(y,x))*(180/np.pi)
    print angle
    
    M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
    dst = cv2.warpAffine(img,M,(width,height))

    dst = binary_img(dst)
    
    return dst

def preprocess(img):
    return skew_correction(img)


cv2.waitKey(0)
cv2.destroyAllWindows()