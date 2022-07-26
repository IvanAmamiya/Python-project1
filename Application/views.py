from  Application import app
from Application import current_app,render_template
from Application import db
name = 'Rokossovskaya'

@app.route('/')
@app.route('/index/')
def index():
  app.logger.info('index')
  return render_template('index.html',useradmin = name)
@app.route('/favicon.ico') 
def favicon():
  return current_app.send_static_file('img/favicon.ico')
@app.route('/Article/')
def Article():
  app.logger.info('Article')
  return render_template('Article.html',useradmin = name)
@app.route('/Shitsumonnhako/')
def Shitsumonnhako():
  app.logger.info('Shitsumonnhako')
  return render_template('Shitsumonnhako.html',useradmin = name)
@app.route('/ShortBlog/')
def ShortBlog():
  app.logger.info('ShortBlog')
  return render_template('ShortBlog.html',useradmin = name)
@app.route('/register/')
def register():
  app.logger.info('register')
  return render_template('register.html',useradmin = name)
@app.route('/login/')
def login():
  app.logger.info('login')
  return render_template('login.html',useradmin = name)


