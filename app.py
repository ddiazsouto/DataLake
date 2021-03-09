
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'

db=SQLAlchemy(app)

class verifyU(FlaskForm):

    login = StringField('Username: ')
    passwd= StringField('Password: ')
    submit= SubmitField('Log in')

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = verifyU()

    if request.method=='POST':

        login = form.login.data
        passwd= form.passwd.data

        if len(passwd)>5:
            return render_template('overview.html', form=form)

    return render_template('login.html', title='Log-in', form=form)



if __name__=='__main__':
    app.run(debug=True)
