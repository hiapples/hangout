from flask import Flask     
from flask import request 
from flask import redirect
from flask import render_template
from flask import Flask, make_response, request,Response
from flask import session
from flask_mail import Mail
from flask_mail import Message
from datetime import datetime, timedelta
from collections import Counter
import random
import smtplib
import time
import json
from flask import*
from bson.objectid import ObjectId
import pymongo
import os
import mailtrap as mt
from flask.views import MethodView
from flask import jsonify
from flask_jwt_extended import JWTManager
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
import bson.binary
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pathlib
from gridfs import *


app = Flask(__name__, static_folder='./static/dist/assets', template_folder='./static/dist')

#測試用帳號
client=pymongo.MongoClient("mongodb+srv://hiapples900:howard900@popalz.bm0pbdd.mongodb.net/?retryWrites=true&w=majority&appName=PoPalz")
db2=client.hangout
collection2=db2.users


#首頁
@app.route('/')
def index():
    return render_template('index.html')
#註冊頁面
@app.route('/signup')
def signup():
    return render_template('signup.html')
#登入頁面
@app.route('/signin')
def signin():
    return render_template('signin.html')

##註冊程序
@app.route("/signuping",methods=["POST"])
def signuping():
    userid=request.form["signup_userid"]
    password=request.form["signup_password"]
    collection2.insert_one({
        "userid":userid,
        "password":password
    })
    return redirect("/signin")
if __name__ == "__main__":
    app.run(debug=True)
