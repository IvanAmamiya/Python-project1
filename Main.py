from flask import Flask,request,jsonify,url_for,redirect,render_template,flash,get_flashed_messages
import logging
from flask import send_from_directory
from logging.handlers import TimedRotatingFileHandler
import config
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'TEST'
name = 'Rokossovskya'
@app.errorhandler(404)
def NOT_FOUND(error):
  app.logger.error(error)
  return render_template('404_NOT_FOUND.html',useradmin = name)

@app.route('/')
@app.route('/index/')
def index():
  app.logger.info('index')
  return render_template('index.html',useradmin = name)
@app.route('/favicon.ico') 
def favicon():
  return 'favicon'

  
if(__name__=='__main__'):
  handler = TimedRotatingFileHandler('Infos.log',interval=15,when='d',backupCount = 15,encoding = 'UTF-8',delay = False,utc = True)
  formatter = logging.Formatter("%(levelname)s: %(asctime)s -%(lineno)d- %(filename)s %(message)s")
  handler.setFormatter(formatter)
  logging.basicConfig(level = logging.DEBUG)
  app.logger.addHandler(handler)
  app.run(host = "127.0.0.1",port = 5000,debug = True,load_dotenv = True)