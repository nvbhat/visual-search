import argparse
import cPickle
import glob
import cv2
import json 
import os, sys
import shutil

#Usage->python imagetojson.py image1,image2,image3....(input one or more images)

#for i in range(1, len(sys.argv)):
    #print str(sys.argv[i])
print "input the json file you want to save!!"
jsonfile = raw_input ()

#writing data to json file manually ......
print "writing data to json file..."

d={
  "book": {
    "title": "",
    "author": "",
    "imagedirpath": "./visual-search/indexedbooks/",
     "images":[],
    "pages": [],
    "annotations" : []
  },

"page": {
  "templateimgpath": "",
    "ncolumns": 2,
    "pagenum": 1,
    "colspace": "10px",
    "linespace": "5px",
    "wordspace": "2px",
    "angle": 30.0,
    "columns": [],
    "annotations" : []
  },

  "column": {
    "geometry": { "startx": 0, "starty": 0, "sizex": 300, "sizey": 300 },
    "title": "",
    "sections": [],
    "annotations" : []
  },
  "section": {
    "geometry": { "startx": 0, "starty": 0, "sizex": 300, "sizey": 300 },
    "title": "",
    "text": "",
    "type": ["paragraph", "footnote", "pagenum", "notes"],
    "lines": [],
    "annotations" : []
  },

 "line": {
          "geometry": { "startx": 0, "starty": 0, "sizex": 300, "sizey": 300 },
  	"text": "",
           "annotations" : [],
  	"phrases": []
          },
  "phrase": {
    "geometry": { "startx": 0, "starty": 0, "sizex": 300, "sizey": 300 },
    "annotations" : []
  },

  "annotation": {
    "author": "",
    "text": "",
    "comment": "",
    "date": "",
    "rank": "0-10",
    "matches": [],
    "see_also": [],
    "refs": []
  }

}


arr = []
for i in range(1, len(sys.argv)):
    #print str(sys.argv[i])
    arr.append(str(sys.argv[i]))

d['book']['images']=arr
json.dumps(d)

with open('visual-search/indexedbooks/'+jsonfile, 'w') as outfile:
     json.dump(d, outfile, sort_keys = True, indent = 2,ensure_ascii=False)
print "Successfully saved!!!"  

#Save all argument-images in a folder("user-uploads") locally to display further
#print arr
for i in arr:
    #print i
    shutil.copy(i, 'visual-search/user-uploads/')
print "images successfully copied"
