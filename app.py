
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField

from formularium import verifyU, new_client, new_employee, new_expense

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'

db=SQLAlchemy(app)










@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = verifyU()
    msg=''

    if request.method=='POST':

        login = form.login.data
        passwd= form.passwd.data

        

        if len(passwd)>5:
            
                return render_template('overview.html', form=form, title='Overview')

        else:
            msg='Please the password is too short'

    return render_template('login.html', title='Log-in', form=form, message=msg)


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    grab_data = new_client()

    if request.method=='POST':

        company_name = grab_data.company_name.data
        contact_name = grab_data.contact_name.data
        contact_surname = grab_data.contact_surname.data
        phone = grab_data.phone.data
        details= grab_data.details.data

            #       Missing the logic in here


    return render_template('sales.html', title='Sales Department', form=grab_data)



@app.route('/new_employee', methods=['GET', 'POST'])
def nemployee():

    grab_data = new_employee()


    if request.method=='POST':
        
        emp_name = grab_data.emp_name.data
        emp_surname= grab_data.emp_surname.data
        role = grab_data.role.data
        team = grab_data.team.data
        department= grab_data.department.data
        

    return render_template('nemployee.html', title='New employee', form=grab_data)


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():

    grab_data = new_expense()

    if request.method=='POST':

        nature = grab_data.nature.data
        vendor = grab_data.vendor.data
        reason = grab_data.reason.data


    return render_template('expenses.html', title='Expenses page', form=grab_data)        





"""     Here the app runs       and lives       not to touch        leave alone     logic above
"""


if __name__=='__main__':
    app.run(debug=True)
