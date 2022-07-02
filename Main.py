from flask import Flask
import config

app = Flask(__name__)

app.config.from_object(config)
@app.route('/index/' ,methods = ['GET'])
def index():
  return {"username":"您1"}

if(__name__=='__main__'):
  app.run(debug = True)