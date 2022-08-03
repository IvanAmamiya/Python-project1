import wtforms
from wtforms.validators import length,EqualTo
from .models import User

class LoginForm(wtforms.Form):
    username = wtforms.StringField()
    password = wtforms.StringField(validators = [length(min = 6,max = 20)])
