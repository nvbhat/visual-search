ROOTDIR = "/tmp/vizdoc"

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
