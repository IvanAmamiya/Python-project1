from flask import Flask,request,jsonify,url_for,redirect,render_template,flash,get_flashed_messages
games = [
{"id":1,"name":"HOI4"},
{"id":2,"name":"CSGO"},
{"id":3,"name":"Dota"},
{"id":4,"name":"EU4"}]
import config
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'TEST'
@app.route('/index/1' ,methods = ['GET'])
def mushroom():
  uid = request.args.get("uid") 
  for game in games:
    if(uid==str(game["id"])):
      return game["name"]
  return "NOT FOUND"
@app.route('/')
@app.route('/index/')
def index():
  res = ''
  for msg in get_flashed_messages():
    res += msg + '<br>'
  res+='hello'
  return res

@app.route('/login/')
def login():
  flash('登陆成功')
  return redirect(url_for('index'))
@app.route('/logout/')
def logout():
  return render_template('logout.html')
@app.errorhandler(404)
def NOT_FOUND(error):
  
    return render_template('404_NOT_FOUND.html')
  
if(__name__=='__main__'):
  app.run(debug = True)