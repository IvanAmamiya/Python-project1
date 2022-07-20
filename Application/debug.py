from Application import app,render_template
name = 'Rokkosovskaya'

@app.errorhandler(404)
def NOT_FOUND(error):
  app.logger.error(error)
  return render_template('404_NOT_FOUND.html',useradmin = name)

