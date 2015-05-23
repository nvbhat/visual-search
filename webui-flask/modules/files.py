import os
from flask import request
from os import path
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *
#import vizdoc_user
#import vizdoc_anno

app = Flask(__name__)

store_api = Blueprint('store_api', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'])
#UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__name__))+'/static/images/'

def allowed_file(filename):
   return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

kusing this we can create, name a book and insert any num. of img files in it and store in appropriate place.The Global "UPLOAD FOLDER" is the location where the new book will be stored. Click "Add Book" in the UI to test it.
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

#add any num. of pages(.jpg files) to an already created book.
@app.route('/uploadpage', methods=['GET', 'POST'])
def upload_file():
# if request.method == 'POST':
    uploaded_files = request.files.getlist("file[]")
    dirname = request.form.get("foldername",None)
    print (dirname)
    #print type(UPLOAD_FOLDER)
    #print type(dirname)
    #BASE_DIR = 'http://localhost:5000' #'/home/vtbhat/vsearch_db'
    #app.config['BASE_DIR'] = '/home/vtbhat/vsearch_db'
    filenames = []
    for file in uploaded_files:
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the upload
            # folder we setup
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(UPLOAD_FOLDER + dirname + filename)
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

#gives the list of all json files, recursively, present in ROOTDIR
@app.route('/getbooklist')
def filelist():
    arr=[]
    for root, dirs, files in os.walk(ROOTDIR):
    #print('Found directory: %s' % root)
        for file in files:
            if file.endswith(".json"):
                 abspath = os.path.join(root,file) 
                 newfile = str.replace(abspath, ROOTDIR, "");
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
    with open(ROOTDIR + jsonfile, 'w') as outfile:
        json.dump(d, outfile, sort_keys = True, indent = 4,ensure_ascii=False)
    # print (s'Successfully saved!')
#    return (d)
    return send_from_directory(ROOTDIR,jsonfile)


#need to be checked
@app.route('/static/<path:filepath>')
def getFile(filepath):
    print "Entered getFile"
    abspath = ROOTDIR + "/" + filepath
    print abspath
    return send_file(abspath)

#returns the book.json showing all of its images
@app.route('/getbooks/<bookid>', methods=['GET','POST'])
def getBook(bookid):
        print "processing " + bookid
        fname = PUBSTORE+"/books/"+bookid+".json"
        print fname
        return send_from_directory(PUBSTORE+"/books",bookid+".json")

#needs to be checked
@app.route('/getpage/<page>', methods=['GET','POST'])
def getpage(page):
    pname = PUBSTORE+"/books/"+page+".json"
    print pname
    image = request.args.get('impath',type=str)
    components = pname.split('/')
    del components[-1]
    extract = components[-1].split('.')
    basename = extract[0]
    extension = "_annotation.json"
    finaljson =  basename + extension
    jsonpath = ROOTDIR + "/"+ '/'.join(components) + "/segments/" + basename + extension
    print jsonpath	
    if path.exists(jsonpath):
        with open(pname) as p:
            bookjson=json.load(f)
        print "all directory files"
        return send_from_directory(PUBSTORE+"/books",basename+".json")

