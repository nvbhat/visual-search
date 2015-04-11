import os
from flask import request
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


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'])

app = Flask(__name__)
#mongo = PyMongo(app, config_prefix='MONGO2')
mongo = PyMongo(app)
# connect to another MongoDB database on the same host
#app.config['MONGO2_DBNAME'] = 'vizdoc_db'
#mongo = PyMongo(app, config_prefix='MONGO2')
global clicked_image

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

#@app.route('/<path:req_path>')
#def dir_listing(req_path):
#    BASE_DIR = ROOTDIR  #'/home/vtbhat/vsearch_db'
#
#    # Joining the base and the requested path
#    abs_path = os.path.join(BASE_DIR, req_path)
#
#    # Return 404 if path doesn't exist
#    if not os.path.exists(abs_path):
#        return abort(404)
#  	
#    # Check if path is a file and serve
#    if os.path.isfile(abs_path):
#        return send_file(abs_path)
#
#    # Show directory contents
#    files = os.listdir(abs_path)
#    return render_template('files.html', files=files)

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

@app.route('/getbooklist')
def filelist():
    arr=[]
    for root, dirs, files in os.walk(ROOTDIR):
    #print('Found directory: %s' % root)
        for file in files:
            if file.endswith(".json"):
                 abspath = os.path.join(root,file) 
                 newfile = str.replace(abspath, ROOTDIR+"/", "");
                 print (newfile)
                 sendpath=newfile
                 data=sendpath[1]

            # print('\t%s' % file)
             #converting RAW data of python array element into json files.
                 arr.append(str(newfile))
#    return '{"books":'+arr+'}'
    print (arr)
    return json.dumps(arr)


    jsonfile = "filelist.json"
    d={
        "paths": ""
      }
    d['paths']=arr
    json.dumps(d)
    print (d)
    with open(ROOTDIR + "/" + jsonfile, 'w') as outfile:
        json.dump(d, outfile, sort_keys = True, indent = 4,ensure_ascii=False)
    # print (s'Successfully saved!')
#    return (d)
    return send_from_directory(ROOTDIR,jsonfile)

@app.route('/static/<path:filepath>')
def getFile(filepath):
    print "Entered getFile"
    abspath = ROOTDIR + "/" + filepath
    print abspath
    return send_file(abspath)

@app.route('/getbooks/<bookid>', methods=['GET','POST'])
def getBook(bookid):
        print "processing " + bookid
        fname = PUBSTORE+"/books/"+bookid+".json"
        print fname
        return send_from_directory(PUBSTORE+"/books",bookid+".json")

@app.route('/saveanno',methods=['GET','POST'])
def saveanno():
    impath = request.args.get('imagepath',type=str)
    coord = request.args.get('coord',type=str)
    mongo.db.annotations.update(
        {'file': impath, 'coord': coord},
        {'ratings': request.get('ratings'), 'name': request.get('name'), 
                    'text': request.get('text'), 'comment': request.get('comment')},
        safe=True, upsert=True)

#def getcontent():
     
@app.route('/<path:pagepath>')
def show_page(pagepath):
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
@app.route('/edit/<path:pagepath>/<coords>', methods=['POST'])
def save_page(pagepath,coords):
    if 'submit' in request.form:
        mongo.db.pages.update(
            {'_id': coords},
            {'$set': {'ratings': request.form['ratings'], 'name': request.form['name'], 'text': request.form['text'], 'com': request.form['com']}},
            safe=True, upsert=True)
    return redirect(url_for('show_page', pagepath=pagepath))

@app.errorhandler(404)
def new_form(error):
    pagepath = clicked_image 
    print pagepath
    coords = request.args.get('pass3',type=str)
    if not coords == "None":
        res = coords
    print res
#    print coords
    if not pagepath.startswith('uploads'):
        return render_template('form.html', page=None, pagepath=pagepath)

@app.route('/getpage/<page>', methods=['GET','POST'])
def getpage(page):
    pname = PUBSTORE+"/books/"+page+".json"
    print pname
    #image = request.args.get('impath',type=str)
    #components = pname.split('/')
    #del components[-1]
    #extract = components[-1].split('.')
    #basename = extract[0]
    #extension = "_annotation.json"
    #finaljson =  basename + extension
#    jsonpath = ROOTDIR + "/"+ '/'.join(components) + "/segments/" + basename + extension
    print jsonpath	
    if path.exists(jsonpath):
        with open(pname) as p:
            bookjson=json.load(f)
        print "all directory files"
        return send_from_directory(PUBSTORE+"/books",basename+".json")

@app.route('/getanno/<coord>',methods=['GET','POST'])
@app.route('/getanno/<coord>/<imagepath>',methods=['GET','POST'])
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


@app.route('/segment',methods=['GET','POST'])
def segment():
    from imagestojson import *
    jsonfile = jsonfile
    clicked_image = request.args.get('imagepath',type=str)
    print clicked_image
    dividing = clicked_image.split('/')
    extract = dividing[-1].split('.')
    imgname = extract[0]
    extension = "_segments.json"
    finaljson =  extract[0]+extension
    jsonpath = "/static/segments/" + finaljson
    if not path.exists(jsonpath):
        rv1 = os.system("python imagestojson.py static/images/"+dividing[-1]) 
        if rv1 == 0: 
            print "one script is succssful"
            rv2 = os.system("python mainimgsegmenter.py -j static/"+jsonfile+" -b "+finaljson) 
    else:
        print "file already exists"
    return jsonify(result=jsonpathi) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    app.run(debug=True)
#    app.run(host = '0.0.0.0',debug=True)  

#def getAnnotations complete

#def delAnnotation

#def genSegments

#def saveAllSegments

#def delSegment
