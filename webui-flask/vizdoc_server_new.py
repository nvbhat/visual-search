#!/usr/bin/python

import os
import sys, getopt
#import requests
from os import path
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime

from vizdoc_config import *
from user import user_api
from docdb import docdb_api
from imgapi import img_api
from filestore import store_api

app = Flask(__name__)

app.register_blueprint(user_api, url_prefix='/users')
app.register_blueprint(docdb_api, url_prefix='/db')
app.register_blueprint(img_api, url_prefix='/process')
app.register_blueprint(store_api, url_prefix='/store')


cmdname = argv[0]
def usage():
    print cmdname + " -r <rootdir> [--addr <ipaddr>[:<port>]]"
    exit(1)

def createdir(dir):
    if not path.exists(dir):
        print "Creating " + dir + " ..." 
        os.mkdir(dir, 0755)

def initstore():
    print "Initializing VizDoc store ..."
    createdir(ROOTDIR)
    createdir(TMPDIR)
    createdir(pubroot())
    createdir(pubimgdir())
    createdir(pubbooksdir())
    createdir(mongodir())
    createdir(cachedir())
    print "done."

@app.route('/')
def home():
    print "Entered home"
    return render_template('home.html')

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"r:ha:",["rootdir=", "addr="])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-r", "--rootdir"):
            ROOTDIR = arg
        elif opt in ("-a", "--addr"):
            outputfile = arg

    print "Using VIZDOC store at " + ROOTDIR
    print "Using VIZDOC tmp folder at " + TMPDIR

    initstore()
    import doctest
    doctest.testmod()
    app.run(host = '0.0.0.0',debug=True)  

if __name__ == "__main__":
   main(sys.argv[1:])
