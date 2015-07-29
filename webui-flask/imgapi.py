import os
from os import path
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *

img_api = Blueprint('img_api', __name__)

@img_api.route('/segment',methods=['GET','POST'])
def segment():
    from imagestojson import *
    jsonfile = jsonfile
    clicked_image = request.args.get('imagepath',type=str)
    dividing = clicked_image.split('/')
    extract = dividing[-1].split('.')
    imgname = extract[0]
    print imgname
    print res
    extension = "_segments.json"
    finaljson =  extract[0]+extension
    jsonpath = "/static/segments/" + finaljson
    if not path.exists(jsonpath):
        rv1 = os.system("python imagestojson.py static/images/"+dividing[-1]) 
        if rv1 == 0: 
            rv2 = os.system("python mainimgsegmenter.py -j static/"+jsonfile+" -b "+finaljson) 
    else:
        print "file already exists"
    return jsonify(result=jsonpath) 
