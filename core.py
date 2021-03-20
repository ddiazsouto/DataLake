from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'   
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Buddhassister22@127.0.0.1/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'


db=SQLAlchemy(app)
