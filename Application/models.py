from Application import app
from Application import SQLAlchemy
from Application import db
HOSTNAME = '127.0.0.1'
PORT     = 3306
DATABASE = 'pythontest'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pysql://{}:{}@{}:{}/{}?charset = utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLAlchemy_DATABASE_URI'] = DB_URI
