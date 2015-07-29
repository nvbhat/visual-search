import os
from os import path
from flask import *
from functools import wraps
import json,time
from werkzeug import secure_filename
#import datetime
from vizdoc_config import *
#import vizdoc_user
#import vizdoc_anno

user_api = Blueprint('user_api', __name__)

@user_api.route('/logged_user')
def logged_home():
    return render_template('hello.html')

#@user_api.route('/welcome')
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

@user_api.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('you were logged out !!')
    return redirect (url_for('login'))

#This is the page which will be opened after login.
@user_api.route('/hello')
@login_required
def hello():
    return render_template('hello.html')


@user_api.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
       if request.form['username'] !='admin' or request.form['password'] !='admin':
          error='Invalid Credentials, Please try again !!'
       else:
           session['logged_in']=True
           return redirect(url_for('hello'))
    return render_template('login.html',error=error)

