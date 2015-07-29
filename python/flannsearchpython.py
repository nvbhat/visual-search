import cv2
import numpy as np
import itertools
import sys
import cv

def findKeyPoints(img, template, distance=200):
    detector = cv2.FeatureDetector_create("SIFT")
    descriptor = cv2.DescriptorExtractor_create("SIFT")

    skp = detector.detect(img)
    skp, sd = descriptor.compute(img, skp)

    tkp = detector.detect(template)
    tkp, td = descriptor.compute(template, tkp)

    flann_params = dict(algorithm=1, trees=4)
    flann = cv2.flann_Index(sd, flann_params)
    idx, dist = flann.knnSearch(td, 1, params={})
    del flann
    for i in range(len(skp)):
        p1_x = skp[i].pt
       
        print p1_x
    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]
    skp_final = []
    for i, dis in itertools.izip(idx, dist):
        if dis < distance:
            skp_final.append(skp[i])

    flann = cv2.flann_Index(td, flann_params)
    idx, dist = flann.knnSearch(sd, 1, params={})
    del flann
    
    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    #print "indices len:",indices
    
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]
    tkp_final = []
    for i, dis in itertools.izip(idx, dist):
        if dis < distance:
            tkp_final.append(tkp[i])
   
    return skp_final, tkp_final

def drawKeyPoints(img, template, skp, tkp, num=-1):
    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1+w2
    nHeight = max(h1, h2)
    hdif = (h1-h2)/2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img

    maxlen = min(len(skp), len(tkp))
    if num < 0 or num > maxlen:
        num = maxlen
    for i in range(num):
	#print "TKP:",tkp[i].pt[0]
        pt_a = (int(tkp[i].pt[0]), int(tkp[i].pt[1]+hdif))
        pt_b = (int(skp[i].pt[0]+w2), int(skp[i].pt[1]))
	#print pt_a[0]

        #one method to draw rectangle
        #p1 = (pt_b[0]-w2,pt_b[1]-(h2/2))
        #p2 = (pt_b[0],pt_b[1]+(h2/2))
        
        #second method for drawing rectangle
        p1=(pt_b[0],pt_b[1])
        p2=(pt_b[0]+w2,pt_b[1]+(h2/2))
        #cv2.rectangle(newimg,p1,p2,(255,0,0),1,cv.CV_AA,0)
        
        #For drawing circle
        pt_final=(pt_b[0],pt_b[1])
        cv2.circle(newimg, pt_final,14,(255, 0, 0),3,8)

        #for draw line
        #cv2.line(newimg, pt_a, pt_b,(255, 0, 0))
    return newimg


def match():
    img = cv2.imread(sys.argv[1])
    temp = cv2.imread(sys.argv[2])
    try:
    	dist = int(sys.argv[3])
    except IndexError:
	print "default distance taken"
    	dist = 200
    try:
    	num = int(sys.argv[4])
    except IndexError:
	print "default number taken"
    	num = -1
    skp, tkp = findKeyPoints(img, temp, dist)
    newimg = drawKeyPoints(img, temp, skp, tkp, num)
    #cv2.imshow("image", newimg)
    cv2.imwrite("result.jpg",newimg)
    cv2.waitKey(0)
    
match()
