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
collection=db2.users

#cls db
#result=collection.delete_many({})

@app.after_request
def add_header(response):
    response.cache_control.max_age = 31536000  # 设置缓存时间，单位为秒
    return response

# 静态文件路由
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue_app(path):
    if path != "" and os.path.exists(app.template_folder + '/' + path):
        return send_from_directory(app.template_folder, path)
    else:
        return send_from_directory(app.template_folder, 'index.html')

# 註冊程序
@app.route("/signuping", methods=["POST"])
def signuping():
    userid = request.form["signup_userid"]
    password = request.form["signup_password"]

    # 查找用戶名是否已經存在
    result = collection.find_one({
        "userid": userid
    })
    if result is not None:
        return jsonify({"success": False, "message": "Username is duplicated"})

    # 將新用戶插入數據庫
    collection.insert_one({
        "userid": userid,
        "password": password
    })

    return jsonify({"success": True, "message": "Registration successful, please log in"})


if __name__ == "__main__":
    app.run(debug=True)
