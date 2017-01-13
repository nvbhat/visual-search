import os, sys
from array import array
import cv2
import numpy as np
import json
import cv
import argparse
import shutil
import preprocessing
from scipy.stats import mode

img = cv2.imread("durga.jpg",0)
img_rgb = preprocessing.binary_img(img)
cv2.imshow("edges",img_rgb)
cv2.waitKey(0)

