from Application import app
from flask_scripe import Manager
manager = Manager(app)
if(__name__=='__main__'):
    manager.run()