from Application import app,TimedRotatingFileHandler,logging,handlers
handler = TimedRotatingFileHandler('./Application/log/Infos.log',interval=1,when='D',backupCount = 15,encoding = 'UTF-8',delay = False,utc = True)
formatter = logging.Formatter("%(levelname)s: %(asctime)s -%(lineno)d- %(filename)s %(message)s")
handler.setFormatter(formatter)
logging.basicConfig(level = logging.DEBUG)
app.logger.addHandler(handler)