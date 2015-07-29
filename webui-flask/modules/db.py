import os
from os import path
from flask.ext.pymongo import PyMongo
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *
#import vizdoc_user
#import vizdoc_anno

app = Flask(__name__)

annodb_api = Blueprint('annodb_api', __name__)

# connect to a MongoDB database on the same host
app.config['MONGO2_DBNAME'] = 'vizdoc_db'
mongo = PyMongo(app, config_prefix='MONGO2')

#deletes annotations in mongodb provided both imagename and coordinates
@annodb_api.route('/delannoimgcoord/<image>',methods=['GET','POST'])
@annodb_api.route('/delannoimgcoord/<image>/<coord>',methods=['GET','POST'])
def delannoimgcord(coord,image=None):
    mongo.db.pages.remove({"imagepath" : image, "coord": coord})
    print "success"
    
#deletes all  annotations related to an image at once 
@annodb_api.route('/delannoimg/<image>',methods=['GET','POST'])
def delannoimg(image):
    mongo.db.pages.remove({"imagepath" : image})
    print "success"

#saves or inserts annotations, used imagepath and coord as keys
@annodb_api.route('/saveanno/<image>/<coord>/<ratings>/<name>/<text>/<comment>',methods=['GET','POST'])
def saveanno(image,coord,ratings,name,text,comment):
#    impath = request.args.get('pagepath',type=str)
#    coord = request.args.get('coord',type=str)
    mongo.db.pages.insert(
        {'imagepath': image, 'coord': coord,
            "annotations" : { "ratings" : ratings, "name" : name, "text" : text, "comment" : comment } },
        safe=True,upsert=True)

#retrives only one annotation, given an imagename.
@annodb_api.route('/retrieveanno/<imagename>')
def retrieveanno(imagename):
    page = mongo.db.pages.find_one_or_404({'imagepath': imagename})
    print page

#updates(replaces annotations for existing keys) an annotation privided an imagepath and coordinates. can be checked using form itself
@annodb_api.route('/form/<coords>',methods=['GET','POST'])
@annodb_api.route('/form/<coords>/<image>',methods=['GET','POST'])
def save_page(coords,image=None):
    if 'submit' in request.form:
        mongo.db.pages.update(
            {'imagepath': image, 'coords': coords},
            {'$set': {'ratings': request.form['ratings'], 'name': request.form['name'], 'text': request.form['text'], 'com': request.form['com']}},
            safe=True, upsert=True)
    return redirect(url_for('show_page', pagepath=pagepath))

@annodb_api.route('/getanno/<coord>',methods=['GET','POST'])
@annodb_api.route('/getanno/<coord>/<imagepath>',methods=['GET','POST'])
def getanno(coord,imagepath=None):
#    impath = request.args.get('imagepath',type=str)
#    coord = request.args.get('coord',type=str)
    print "getting mongodb contents"
    anno = mongo.db.annotations.find_one_or_404({'coord':coord,'imagepath':imagepath})
    print "successful"
    print anno
#        {'ratings': request.get('ratings'), 'name': request.get('name'), 
#                    'text': request.get('text'), 'comment': request.get('comment')},
#        safe=True, upsert=True)
