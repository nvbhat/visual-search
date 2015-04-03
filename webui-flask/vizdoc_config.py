ROOTDIR = "/home/vtbhat/vsearch_db"

MONGODIR = ROOTDIR + "/mongodb"

CACHEDIR = ROOTDIR + "/cache"

USERSTORE = ROOTDIR + "/users"

PUBSTORE = ROOTDIR + "/public"

def userimgdir(user):
    USERSTORE + "/" + user + "/images"

def userbooksdir(user):
    USERSTORE + "/" + user + "/books"
