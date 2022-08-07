from Application import app
from Application import SQLAlchemy
from Application import db
from sqlalchemy import Column, Integer, String 
import random
from datetime import datetime
from werkzeug.security import generate_password_hash
HOSTNAME = '0.0.0.0'
PORT     = 3306
DATABASE = '1'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pysql://{}:{}@{}:{}/{}?charset = utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLAlchemy_DATABASE_URI'] = DB_URI
app.config['SECRET_KEY'] = '114s'
db.drop_all()
class User(db.Model):  
    
        __tablename__ = "user"
        id = db.Column(db.Integer,primary_key = True,autoincrement = True)
        username = db.Column(db.String(200),nullable = False,unique = True)
        password = db.Column(db.String(200),nullable = False,unique = False)

class BlogModel(db.Model):  
    
        __tablename__ = "Blogs"
        id = db.Column(db.Integer,primary_key = True,autoincrement = True)
        type = db.Column(db.String(400),nullable = False)
        title = db.Column(db.String(200),nullable = False)
        Author = db.Column(db.String(200),nullable = False)
        content = db.Column(db.String(200),nullable = False)
        Creat_Date = db.Column(db.String(200),default = datetime.now(),nullable = False)
#User1 = User(username = "System_Admin",password = generate_password_hash("PoWm1147h"))
#db.session.add(User1)
#db.session.commit()
class ReviewModel(db.Model):
        __tablename__ = "review"
        id = db.Column(db.Integer,primary_key = True,autoincrement = True)
        Author = db.Column(db.String(200),nullable = False)
        content = db.Column(db.String(200),nullable = False)
        Creat_Date = db.Column(db.String(200),default = datetime.now(),nullable = False)
        type = db.Column(db.String(200),nullable = False)
     
        Blog_id = db.Column(db.Integer,db.ForeignKey("Blogs.id"))

        Blog = db.relationship("BlogModel",backref = db.backref("reviews"))



db.create_all()




