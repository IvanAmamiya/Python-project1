from flask import Flask,request,jsonify,url_for,redirect,render_template
games = [
{"id":1,"name":"HOI4"},
{"id":2,"name":"CSGO"},
{"id":3,"name":"Dota"},
{"id":4,"name":"EU4"}]
import config
app = Flask(__name__)
app.config.from_object(config)
@app.route('/index/1' ,methods = ['GET'])
def mushroom():
  uid = request.args.get("uid") 
  for game in games:
    if(uid==str(game["id"])):
      return game["name"]
  return "NOT FOUND"
@app.route('/index/')
def index():
  return "Index"
@app.route('/login/')
def login():
  return render_template('login.html')
@app.route('/logout/')
def logout():
  return render_template('logout.html')
if(__name__=='__main__'):
  app.run(debug = True)