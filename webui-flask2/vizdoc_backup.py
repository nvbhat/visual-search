from __future__ import * 
import os
import requests
from os import path
from flask import Flask,g,render_template, url_for,request,jsonify
from flask.ext.pymongo import PyMongo
import markdown
import re
#from bson import json_util
#from bson.objectid import ObjectId
#from pymongo import MongoClient,Connection
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
import imagestojson
#UPLOAD_FOLDER = '/home/vtbhat/vsearch_db/public'
#UPLOAD_FOLDER = 'http://localhost:5000/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'])
app = Flask(__name__)
mongo = PyMongo(app)
 
#app.config['UPLOAD_FOLDER'] = "/home/vtbhat/vsearch_db"
global res
UPLOAD_FOLDER = '/home/vtbhat/visual-search/vsearch_db/public/'
#PUBSTORE = 
#print UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
##    if request.method == 'POST':
  #      file = request.files.getlist('file[]')
   #     if file and allowed_file(file.filename):
    #        filename = secure_filename(file.filename)
     #       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      #      return redirect(url_for('uploaded_file',
       #                             filename=filename))
#    return render_template('upload.html') 

@app.route('/uploadbook', methods=['GET', 'POST'])
def upload_book():
#    if request.method == 'POST':
    uploaded_files = request.files.getlist("file[]")
    dirname = request.form.get("foldername",None)
    print (dirname)
    #print type(UPLOAD_FOLDER)
    #print type(dirname)
    #BASE_DIR = 'http://localhost:5000' #'/home/vtbhat/vsearch_db'
    #app.config['BASE_DIR'] = '/home/vtbhat/vsearch_db'
    if not dirname == None:
    	abs_path = UPLOAD_FOLDER + dirname + '/'
    	print (abs_path)
    	if not os.path.exists(abs_path):
    	    os.mkdir(abs_path)
    	else:
                return "A book with this name already exists.. Please give another name."
    filenames = []
    for file in uploaded_files:
      	# Check if the file is one of the allowed types/extensions
       	if file and allowed_file(file.filename):
     	    # Make the filename safe, remove unsupported chars
       	    filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the upload
            # folder we setup
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       	    file.save(abs_path + filename)
       	    filenames.append(filename)
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            #return "file(s) uploaded successfully"
    # Load an html page with a link to each uploaded file
    #return redirect(url_for('uploaded_files', filename=filename))
    #return redirect(url_for('dir_listing', dirname=dirname))
    return render_template('uploadbook.html',filenames=filenames)

@app.route('/getBook', methods=['GET','POST'])
def helloService():
        path = os.walk("/home/vtbhat/visual-search/webui-flask/static/visual-search/images")
        for root, dirs, files in path:
            for file in files:
                if file.endswith(".jpg"):
                    return print(os.path.join(root, file))
#        with open("/home/vtbhat/visual-search/python/visual-search/indexedbooks/booklist"+id+".json") as f:
#            bookjson=json.load(f)
#            return bookjson

@app.route('/uploadpage', methods=['GET', 'POST'])
def upload_file():
#    if request.method == 'POST':
    uploaded_files = request.files.getlist("file[]")
    dirname = request.form.get("foldername")
    print (dirname)
    #print type(UPLOAD_FOLDER)
    #print type(dirname)
    #BASE_DIR = 'http://localhost:5000' #'/home/vtbhat/vsearch_db'
    #app.config['BASE_DIR'] = '/home/vtbhat/vsearch_db'
    abs_path = UPLOAD_FOLDER + dirname + '/'
    print (abs_path)
    filenames = []
    for file in uploaded_files:
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the upload
            # folder we setup
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(abs_path + filename)
            filenames.append(filename)
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            #return "file(s) uploaded successfully"
    # Load an html page with a link to each uploaded file
    #return redirect(url_for('uploaded_files', filename=filename))
    #return redirect(url_for('dir_listing', dirname=dirname))
    return render_template('uploadpage.html',filenames=filenames)


@app.route('/upload/<filename>')
def uploaded_files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/uploads', defaults={'req_path': UPLOAD_FOLDER}) #'/home/vtbhat/vsearch_db'})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = UPLOAD_FOLDER #'/home/vtbhat/vsearch_db'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)
  	
    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)

app.secret_key = 'milan322'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logged_user')
def logged_home():
    return render_template('hello.html')

#@app.route('/welcome')
#def welcome():
#   return render_template('welcome.html')


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('you need to login first!')
            return redirect(url_for('login'))
    return wrap 

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('you were logged out !!')
    return redirect (url_for('login'))

@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')


@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
       if request.form['username'] !='admin' or request.form['password'] !='admin':
          error='Invalid Credentials, Please try again !!'
       else:
           session['logged_in']=True
           return redirect(url_for('hello'))
    return render_template('login.html',error=error)
      
@app.route('/<path:pagepath>')
def show_page(pagepath,coords):
    page = mongo.db.pages.find_one_or_404({'_id': pagepath})
    return render_template('form.html',
        page=page,
        pagepath=pagepath)

@app.route('/edit/<path:pagepath>', methods=['GET'])
def edit_page(pagepath):
    page = mongo.db.pages.find_one_or_404({'_id': pagepath})
    return render_template('form.html',
        page=page,
        pagepath=pagepath)

@app.route('/edit/<path:pagepath>', methods=['POST'])
def save_page(pagepath,coords):
    if 'submit' in request.form:
        mongo.db.pages.update(
            {'_id': coords},
            {'$set': {'ratings': request.form['ratings'], 'name': request.form['name'], 'text': request.form['text'], 'com': request.form['com']}},
            safe=True, upsert=True)
    return redirect(url_for('show_page', pagepath=pagepath))

@app.errorhandler(404)
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

#@app.route('/coords',methods=['GET','POST'])
#def coords():
#    coords = request.args.get('pass3',type=str)
#    print coords
#    return render_template('form.html',coords=coords)

@app.route('/segment',methods=['GET','POST'])
def segment():
    jsonfile = imagestojson.jsonfile
    clicked_image = request.args.get('imagepath',type=str)
    dividing = clicked_image.split('/')
    extract = dividing[-1].split('.')
    imgname = extract[0]
    print imgname
    print res
    extension = "_segments.json"
    finaljson =  extract[0]+extension
    jsonpath = "/static/visual-search/segmented-books/"+finaljson
    if not path.exists(jsonpath):
        rv1 = os.system("python imagestojson.py static/visual-search/images/"+dividing[-1]) 
        if rv1 == 0: 
            rv2 = os.system("python mainimgsegmenter.py -j static/visual-search/indexedbooks/"+jsonfile+" -b "+finaljson) 
    else:
        print "file already exists"
    return jsonify(result=jsonpath) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
#    app.run(debug=True)
    app.run(host = '192.168.1.15')  

#def saveAnnotation

#def getAnnotations

#def delAnnotation

#def genSegments

#def saveAllSegments

#def delSegment
