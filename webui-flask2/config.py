import os
from os import path
from os.path import *
import re

ROOTDIR = "/tmp/vizdoc"
PORTNUM = 9000

def mongodir():
    return ROOTDIR + "/mongodb"

def cachedir():
    return ROOTDIR + "/cache"

def userroot(user):
    return ROOTDIR + "/users/" + user

def userimgdir(user):
    return userroot(user) + "/images"

def userbooksdir(user):
    return userroot(user) + "/books"

def pubroot():
    return ROOTDIR + "/public"

def pubimgdir():
    return pubroot() + "/images"

def pubbooksdir():
    return pubroot() + "/books"

def workdir():
    return ROOTDIR

def setworkdir(arg):
    global WORKDIR
    print "Setting root working directory to " + arg
    WORKDIR = arg

def createdir(dir):
    if not path.exists(dir):
        print "Creating " + dir + " ..." 
        try:
            os.makedirs(dir, 0755)
        except Exception as e:
            print "Error: cannot create directory, aborting.\n",e
            pass

def initworkdir(reset):
    if (reset):
        print "Clearing previous contents of " + workdir()
        os.system("rm -rf " + workdir());

    print "Initializing work directory ..."
    createdir(workdir())
    createdir(pubroot())
    createdir(workdir() + "/users")
    createdir(dbdir())
    createdir(wloaddir())
    print "done."

def addrepo(d, reponame):
    if not isdir(d):
        return

    targetdir = pubbooksdir();
    if reponame:
        targetdir = join(targetdir, reponame)
        createdir(dirname(targetdir))
    cmd = "ln -s " + realpath(d) + " " + targetdir
    os.system(cmd)
