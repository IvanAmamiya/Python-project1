from  Application import app,session,request,redirect,flash
from Application import current_app,render_template,url_for
from Application import db,g
from .forms import LoginForm,QBOX_Form,Article_Form,Review_Form,Answer_Form
from werkzeug.security import check_password_hash
from .models import User,BlogModel,ReviewModel
from .decorators import  Authorize_Confirmed
from datetime import datetime
from sqlalchemy import or_

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
  questions = BlogModel.query.order_by(db.text("-id")).all()
  app.logger.info('index')
  return render_template('index.html',useradmin = name,questions = questions)
@app.route('/favicon.ico') 
def favicon():
  return current_app.send_static_file('img/favicon.ico')
@app.route('/Article/',methods = ["GET","POST"])
@Authorize_Confirmed
def Article():
  app.logger.info('Article')
  if(request.method == "GET"):
    return render_template('Article.html',useradmin = name)
  else:
    form_Article = Article_Form(request.form)
    if form_Article.validate():
      title = form_Article.title.data
      content = form_Article.content.data
      Commit_Article = BlogModel(title = title,type = "Article",Author = name,content = content,Creat_Date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
      db.session.add(Commit_Article)
      db.session.commit()
      return redirect(url_for("Article_index"))
    else:
        flash("格式错误……您管理员不会不清楚吧")
        return redirect(url_for("Article"))


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
      question = BlogModel(title = title,Author = Author,type = "question",content = content,Creat_Date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
      db.session.add(question)
      db.session.commit()
      return redirect(url_for("index"))
    else:
        flash("格式错误……内容少填了 标题和署名太长了(最小1最大20)等等")
        return redirect(url_for("Shitsumonnhako"))

@app.route("/Shitsumonnhako_index")
def Shitsumonnhako_index():
  Questions = BlogModel.query.filter_by(type = "question").order_by(db.text("-id")).all()
  app.logger.info('Shitsumonnhako_index')
  return render_template('Shitsumonnhako_index.html',useradmin = name,Questions = Questions)
@app.route('/Article_index/')
def Article_index():
  Articles = BlogModel.query.filter_by(type = "Article").order_by(db.text("-id")).all()
  app.logger.info('Article_index')
  return render_template('Article_index.html',useradmin = name,Articles = Articles)
   
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
@app.route("/Blog/<int:Blog_id>")
def Blog_detail(Blog_id):
  Blog = BlogModel.query.filter_by(id = Blog_id).first()
  Blog.reviews = ReviewModel.query.order_by(db.text("-id")).all()

  return render_template("detail.html",Blog= Blog,useradmin = name)
@app.route("/Review",methods = ["POST"])
def Review():
  id = request.args.get('id', '')
  Blog = BlogModel.query.filter_by(id = id).first()
  
  reviews_form = Review_Form(request.form)
  if reviews_form.validate():
    Author = reviews_form.Author.data
    content = reviews_form.content.data
    reviews = ReviewModel(Author = Author,content = content,Creat_Date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),Blog_id = id,type = "guest")
    db.session.add(reviews)
    db.session.commit()
    return render_template("detail.html",Blog_id = id,Blog = Blog,review = reviews,useradmin = name)
  else:
    flash("格式错误……署名和内容格式错误")
    return render_template("detail.html",Blog_id = id,Blog = Blog ,review = reviews ,useradmin = name)
@app.route("/Answer",methods = ["POST"])
def Answer():
  id = request.args.get('id', '')
  Blog = BlogModel.query.filter_by(id = id).first()

  Answers_form = Answer_Form(request.form)
  Answers_form.Author = name
  if Answers_form.validate():
    Author = name
    content = Answers_form.content.data
    answers = ReviewModel(Author = Author,content = content,Creat_Date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),Blog_id = id,type = "admin")
    db.session.add(answers)
    db.session.commit()
    return render_template("detail.html",Blog_id = id,Blog = Blog,useradmin = name)
  else:
    flash("格式错误……署名和内容格式错误")
    return render_template("detail.html",Blog_id = id,Blog = Blog ,useradmin = name)
@app.route("/search",methods = ["GET"])
def search():
    Q = request.args.get("Q")
    Blog = BlogModel.query.filter(or_(BlogModel.title.contains(Q),BlogModel.content.contains(Q)))
    return render_template("index.html",questions = Blog,useradmin = name)








