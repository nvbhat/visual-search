import os, sys
import glob
import cv2
import numpy as np

dir_list = ["./testimages/"]
while len(dir_list) > 0:
    cur_dir = dir_list[0]
    del dir_list[0]
    list_of_files = glob.glob(cur_dir+"*")
    for book in list_of_files:
        if os.path.isfile(book):
            print(book)
            img=cv2.imread(book)
            cv2.imshow('image',img)
            cv2.waitKey(0)
        else:
            dir_list.append(book)
