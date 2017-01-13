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


cmdname = sys.argv[0]
def usage():
    print cmdname + " -r <rootdir> [--addr <ipaddr>[:<port>]]"
    exit(1)

def createdir(dir):
    if not path.exists(dir):
        print "Creating " + dir + " ..." 
        os.mkdir(dir, 0755)

def initstore():
    print "Initializing VizDoc store ..."
    createdir(workdir())
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
    if len(argv) < 1:
        usage()
    try:
        opts, args = getopt.getopt(argv,"o:p:rh",["workdir="])
    except getopt.GetoptError:
        usage()

    reset = False
    myport = PORTNUM
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-o", "--workdir"):
            setworkdir(arg)
        elif opt in ("-p", "--port"):
            myport = int(arg)
        elif opt in ("-r", "--reset"):
            reset = True

    print cmdname + ": Using " + workdir() + " as working directory."
    
    initworkdir(reset)
    for a in args:
        components = a.split(':')
        if len(components) > 1:
            print "Importing " + components[0] + " as " + components[1]
            addrepo(components[0], components[1])
        else: 
            print "Importing " + components[0]
            addrepo(components[0], "")
    
    os.chdir(workdir())

    app.run(
      host ="0.0.0.0",
      port = myport,
      debug = True,
      use_reloader=False
     )

if __name__ == "__main__":
   main(sys.argv[1:])
