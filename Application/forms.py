import wtforms
from wtforms.validators import length,EqualTo
from .models import User
from flask import g

class LoginForm(wtforms.Form):
    username = wtforms.StringField()
    password = wtforms.StringField(validators = [length(min = 6,max = 20)])
class QBOX_Form(wtforms.Form):
    title = wtforms.StringField(validators = [length(min = 1,max = 30)])
    Author = wtforms.StringField(validators = [length(min = 1,max = 16)])
    content = wtforms.StringField()
class Article_Form(wtforms.Form):
    title = wtforms.StringField(validators = [length(min = 1,max = 30)])
    content = wtforms.StringField()
class Review_Form(wtforms.Form):
    id = wtforms.StringField()
    Author = wtforms.StringField(validators = [length(min = 1,max = 16)])
    content = wtforms.StringField()
class Answer_Form(wtforms.Form):
    id = wtforms.StringField()
    content = wtforms.StringField()

                        