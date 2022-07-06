from flask import Flask,request,jsonify,url_for,redirect,render_template,flash,get_flashed_messages
import logging
from logging.handlers import TimedRotatingFileHandler
import config
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'TEST'
name = 'Rokossovskya'
@app.route('/')
@app.route('/index/')
def index():
  app.logger.info('a')
  return render_template('index.html',useradmin = name)

@app.errorhandler(404)
def NOT_FOUND(error):
  app.logger.error('404')
  return render_template('404_NOT_FOUND.html',useradmin = name)

  
if(__name__=='__main__'):
  handler = TimedRotatingFileHandler('Infos.log',interval=1,when='d',backupCount = 15,encoding = 'UTF-8',delay = False,utc = True)
  formatter = logging.Formatter("%(asctime)s - %(message)s")
  handler.setFormatter(formatter)
  app.logger.addHandler(handler)
  app.run(debug = True)