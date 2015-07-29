from __future__ import print_function
import json 
import os, sys,posixpath
rootdir = "./dbs"
arr=[]
arr2=[]
for root, dirs, files in os.walk(rootdir):
    #print('Found directory: %s' % root)
    for file in files:
        if file.endswith(".json"):
             basepath = posixpath.join(root,file)
             sendpath=basepath.split('/')
             sendpath.append(sendpath)
             data=sendpath[1]
            # print('\t%s' % file)
             #converting RAW data of python array element into json files.
             arr.append(str(data))



jsonfile = "filelist.json"

d={
    "filelist": {
        "paths": "",
        }
    }

#print(arr)
for i in range(0,len(arr)):
    strdata=arr[i]
    print("Ori :",strdata)
    strdata.replace("\\","/")
    print("Dub : ",strdata)
    arr2.append(strdata)



d['filelist']['path']=arr
json.dumps(d)
#print(arr2)
with open(jsonfile, 'w') as outfile:
    json.dump(d, outfile, sort_keys = True, indent = 4,ensure_ascii=False)
# print (s'Successfully saved!')
