from  Application import app
from Application import current_app,render_template
name = 'Rokossovskaya'

@app.route('/')
@app.route('/index/')
def index():
  app.logger.info('index')
  return render_template('index.html',useradmin = name)
@app.route('/favicon.ico') 
def favicon():
  return current_app.send_static_file('img/favicon.ico')
