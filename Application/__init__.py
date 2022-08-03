
from flask import Flask,request,jsonify,url_for,redirect,render_template,flash,get_flashed_messages
import logging,os
from flask import current_app
from logging.handlers import TimedRotatingFileHandler
import config
from logging import handlers
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)


from Application import views,models,debug,loggings

