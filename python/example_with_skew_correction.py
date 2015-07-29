
import cv2
import prep2


img1 = cv2.imread('1.jpg',0)
cv2.imshow('Output0',img1)
prep_img1 = prep2.preprocess(img1)
cv2.imshow('Output1',prep_img1)
cv2.imwrite('skewres1_prec.jpg',prep_img1)

img2 = cv2.imread('Kandanu10.jpg',0)
prep_img2 = prep2.preprocess(img2)
cv2.imshow('Outpu2t',prep_img2)
cv2.imwrite('skewres2_prec.jpg',prep_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

