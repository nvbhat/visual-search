import cv2
import sys,os
import preprocessing
import numpy as np
import json
import argparse
import cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
		       help = "Path to the directory that contains image file")

ap.add_argument("-b", "--book", required = True,
		help = "give a json file name to store the segmented result(ex:->filename.json)")

ap.add_argument("-d", "--dir", required = True,
		help = "temporary directory")


args = vars(ap.parse_args())
imagefile = args["image"]
segbookfilename = args['book']
root_dir= args['dir']
image=root_dir+"/example-images/user_uploads/"+imagefile
bookdir_segresult=root_dir+"/tmp/segmented-books/"
resultimgdir= root_dir+"/tmp/segmented-images/"
#imagename=os.path.basename( imagefile)

splitimagename=imagefile.split(".")
resultimagename=splitimagename[0]+"-result.jpg"

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 


img = cv2.imread(image,0)
resultimage = cv2.imread(image)

#cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)
boxes_temp = np.zeros(img.shape[:2],np.uint8)

binary = preprocessing.binary_img(img)
#cv2.imshow('Outputimg1',binary)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
#cv2.imshow('Outputimg2',dilation)

erosion = cv2.dilate(dilation,kernel1,iterations = 1)
#cv2.imshow('Outputimg3',erosion)

edges = cv2.Canny(dilation,50,100)
#cv2.imshow('edges',edges)          

dilation2 = cv2.dilate(edges,kernel1,iterations = 1)
#cv2.imshow('Outputimg9999',dilation2)

inv9999 = 255-dilation2
#cv2.imshow('inv9999',inv9999)

edges = cv2.dilate(edges,kernel1,iterations = 1)
ret,thresh = cv2.threshold(erosion,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #cv2.rectangle(boxes_temp,(x,y),(x+w,y+h),(255,255,255),-1)
    if h> 10:
        all_heights.append(h)

#print all_heights
std_dev = np.std(all_heights)
mn = np.mean(all_heights)
md = np.median(all_heights)
#print std_dev,mn, md

for xx in contours:
    cv2.drawContours(edges,[xx],-1,(255,255,255),-1)
    
#cv2.imshow('edges2',edges)


ret,thresh = cv2.threshold(erosion,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #if (mn+(std_dev/2)<h):
    cv2.rectangle(boxes_temp,(x,y),(x+w,y+h),(255,0,0),-1)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
#cv2.imshow('boxes_temp',boxes_temp)


ret,thresh = cv2.threshold(boxes_temp,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

f= open(bookdir_segresult+segbookfilename,'w')
nMatches=0
str2="\n{\n    \"imagepath\": "+"\""+bookdir_segresult+"\""+","
f.write(str2) 
str3= "\n    \"segments\":[\n"
f.write(str3)



for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(resultimage,(x,y),(x+w,y+h),(0,0,255),2)
    if(nMatches != 0):
       f.write(",")
    str4 = "\n\t{"+"     \"geometry\":"+"{"+"\"x\":"+str(x)+","+"\"y\":"+str(y)+","+"\"height\":"+str(h)+","+"\"width\":"+str(w)+ "}"+"}"
    f.write(str4)
    nMatches = nMatches+1
str5="\n]\n}\n"
f.write(str5)
f.close()

#cv2.imshow('img',resultimage)
#cv2.imshow('img',img)
cv2.imwrite(resultimgdir+resultimagename,resultimage)
print bookdir_segresult+segbookfilename
cv2.waitKey(0)
cv2.destroyAllWindows()
