from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField







class verifyU(FlaskForm):

    login = StringField('Username: ')
    passwd= StringField('Password: ')
    submit= SubmitField('Log in')

class new_client:

    name = StringField('')