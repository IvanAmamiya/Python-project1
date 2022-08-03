from  Application import app,session,request,redirect,flash
from Application import current_app,render_template,url_for
from Application import db,g
from .forms import LoginForm,QBOX_Form
from werkzeug.security import check_password_hash
from .models import User,QuestionBox
name = 'Rokossovskaya'

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if (user_id):
        try:
            user = User.query.get(user_id)
            setattr(g,"user",user)
        except:
            pass
@app.context_processor
def context_processor():
    if(hasattr(g,"user")):
        return {"user":g.user}
    else:
        return {}

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

@app.route('/Shitsumonnhako/',methods = ["GET","POST"])
def Shitsumonnhako():
  app.logger.info('Shitsumonnhako')
  if(request.method == "GET"):
    return render_template('Shitsumonnhako.html',useradmin = name)
  else:
    form = QBOX_Form(request.form)
    if form.validate():
      title = form.title.data
      Author = form.Author.data
      content = form.content.data
      question = QuestionBox(title = title,Author = Author,content = content)
      db.session.add(question)
      db.session.commit()
      return redirect(url_for("index"))
    else:
        flash("格式错误！")
        return redirect(url_for("Shitsumonnhako"))

@app.route('/ShortBlog/')
def ShortBlog():
  app.logger.info('ShortBlog')
  return render_template('ShortBlog.html',useradmin = name)
@app.route('/register/')
def register():
  app.logger.info('register')
  return render_template('register.html',useradmin = name)
@app.route('/login/',methods = ["GET","POST"])
def login():
  app.logger.info('login')
  if(request.method == "GET"):
    return render_template('login.html',useradmin = name)
  else:
    form = LoginForm(request.form)
    if form.validate():
      username = form.username.data
      password = form.password.data
      user = User.query.filter_by(username = username).first()
      if (user and check_password_hash(user.password, password)):
        session['user_id'] = user.id
        return redirect(url_for("index"))
      else:
        flash("用户名或密码错误")
        return redirect(url_for("login"))
    else:
      flash("用户名或密码错误")
      return redirect(url_for("login"))
@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for("login"))




