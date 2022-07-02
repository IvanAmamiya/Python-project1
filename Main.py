from flask import Flask
import config

app = Flask(__name__)

app.config.from_object(config)
@app.route('/index/')

def index():
  return {"username":"您"}

if(__name__=='__main__'):
  app.run(debug = False)