
from flask import Flask,request,jsonify,url_for,redirect,render_template,flash,get_flashed_messages,session
import logging,os
from flask import current_app,flash,g
from logging.handlers import TimedRotatingFileHandler
import config
from logging import handlers
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)
migrate = Migrate(app,db)


from Application import views,models,debug,loggings

