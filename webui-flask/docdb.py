import os
from os import path
from flask.ext.pymongo import PyMongo
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *

app = Flask(__name__)

docdb_api = Blueprint('docdb_api', __name__)

# connect to another MongoDB database on the same host
app.config['MONGO2_DBNAME'] = 'vizdoc_db'
mongo = PyMongo(app, config_prefix='MONGO2')

@docdb_api.route('/saveanno',methods=['GET','POST'])
def saveanno():
    impath = request.args.get('imagepath',type=str)
    coord = request.args.get('coord',type=str)
    mongo.db.annotations.update(
        {'file': impath, 'coord': coord},
        {'ratings': request.get('ratings'), 'name': request.get('name'), 
                    'text': request.get('text'), 'comment': request.get('comment')},
        safe=True, upsert=True)

@docdb_api.route('/getanno',methods=['GET','POST'])
def getanno():
    impath = request.args.get('imagepath',type=str)
    coord = request.args.get('coord',type=str)
    anno = mongo.db.annotations.find_one(
        {'file': impath, 'coord': coord})
    return anno 
#        {'ratings': request.get('ratings'), 'name': request.get('name'), 
#                    'text': request.get('text'), 'comment': request.getdb.dropDatabase()('comment')},
#        safe=True, upsert=True)

"""      
@docdb_api.route('/<path:pagepath>')
def show_page(pagepath):
    page = mongo.db.pages.find_one_or_404({'_id': pagepath})
    return render_template('form.html',
        page=page,
        pagepath=pagepath)

@docdb_api.route('/edit/<path:pagepath>', methods=['GET'])
def edit_page(pagepath):
    page = mongo.db.pages.find_one_or_404({'_id': pagepath})
    return render_template('form.html',
        page=page,
        pagepath=pagepath)


@docdb_api.route('/edit/<path:pagepath>', methods=['POST'])
def save_page(pagepath,coords):
    if 'submit' in request.form:
        mongo.db.pages.update(
            {'_id': coords},
            {'$set': {'ratings': request.form['ratings'], 'name': request.form['name'], 'text': request.form['text'], 'com': request.form['com']}},
            safe=True, upsert=True)
    return redirect(url_for('show_page', pagepath=pagepath))

@docdb_api.errorhandler(404)
def new_form(error):
    pagepath = request.path.lstrip('/')
    print pagepath
    coords = request.args.get('pass3',type=str)
    if not coords == "None":
        res = coords
    print res
#    print coords
    if not pagepath.startswith('uploads'):
        return render_template('form.html', page=None, pagepath=pagepath)
"""

#def getAnnotations

#def delAnnotation

#def genSegments

#def saveAllSegments

#def delSegment
