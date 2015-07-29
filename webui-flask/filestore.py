import os
from os import path
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *

store_api = Blueprint('store_api', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'])
 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#@store_api.route('/upload', methods=['GET', 'POST'])
#def upload_file():
##    if request.method == 'POST':
  #      file = request.files.getlist('file[]')
   #     if file and allowed_file(file.filename):
    #        filename = secure_filename(file.filename)
     #       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      #      return redirect(url_for('uploaded_file',
       #                             filename=filename))
#    return render_template('upload.html') 

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

@store_api.route('/uploadbook', methods=['GET', 'POST'])
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

@store_api.route('/getbooks/<bookid>', methods=['GET','POST'])
def getBook(bookid):
        print "processing " + bookid
        fname = PUBSTORE+"/books/"+bookid+".json"
        print fname
	return send_from_directory(PUBSTORE+"/books",bookid+".json")

@store_api.route('/uploadpage', methods=['GET', 'POST'])
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


@store_api.route('/upload/<filename>')
def uploaded_files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@store_api.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = ROOTDIR  #'/home/vtbhat/vsearch_db'

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

@store_api.route('/static/<path:filepath>')
def getFile(filepath):
    abspath = ROOTDIR + "/" + filepath
    print abspath
    return send_file(abspath)

