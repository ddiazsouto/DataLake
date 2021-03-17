# External modules
import pymysql
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
# Those were the external modules 

# Internal modules:
from formularium import verifyU, new_client, new_employee, new_expense
from elementae import Usuarium, DanSQL

# Those were the internal modules


"""
Up here the app and database configuration are defined as well as their connections to python

First the connection the database through SQLAlchemy

"""


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'    ---->>> Original (this one goes to production and to the cloud)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Buddhassister22@127.0.0.1/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'


db=SQLAlchemy(app)



# Make=pymysql.connect(host='34.121.192.21', user='root', passwd='645202398', db='main')    <<<----  Use this for presentation, this one goes to the cloud
# Make=pymysql.connect(host='127.0.0.1', user='root', passwd='Buddhassister22', db='main')
# MySQL=Make.cursor()
# #                        I need to make this into an object
# def sudo():
#     Make.commit()

"""
Now some logic for the app and its routes

"""


user = Usuarium()                         # We create an object to control the user login

MySQL=DanSQL()






@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():



    form = verifyU()
    msg=''

    if request.method=='POST':

        
        if user.check(form.login.data, form.passwd.data ) == True:


            if user.department() == 'Sales':
                return render_template('dpt-sales.html', form=form, title='Sales', name=user.name(), department=user.department(), user=user)

            elif user.department() == 'HR':
                return render_template('dpt-hr.html', form=form, title='HR', name=user.name(), department=user.department(), user=user)


        else:
            msg='Please, that is a wrong username'

    return render_template('login.html', title='Log-in', form=form, message=msg)





@app.route('/add-client', methods=['GET', 'POST'])
def client():

    grab_data = new_client()
    msg=''

    if request.method=='POST':

        
        company_name = grab_data.company_name.data        #   Assigning value
        contact_name = grab_data.contact_name.data        #   to the variables    
        contact_surname = grab_data.contact_surname.data  #   internally
        phone = grab_data.phone.data                      #   so we can 
        details= grab_data.details.data                   #   manipulate them
                                                        # with posterior logic
        
        if len(contact_name)*len(company_name)*len(phone) != 0:

            MySQL.write(f"INSERT INTO client(company_name, contact_name, contact_surname, phone, details) VALUES('{company_name}','{contact_name}','{contact_surname}','{phone}','{details}');")
            
            grab_data.company_name.data = grab_data.contact_name.data = grab_data.contact_surname.data = ''
            grab_data.phone.data = grab_data.details.data = ''

            msg = 'New client added'

        else:
            msg='Please, fill in all required fields'


    return render_template('client.html', title='New Client', message=msg,  form=grab_data, user=user)



@app.route('/new-employee', methods=['GET', 'POST'])
def nemployee():

    grab_data = new_employee()
    msg =''


    if request.method=='POST':
        
        emp_name = grab_data.emp_name.data
        emp_surname= grab_data.emp_surname.data
        role = grab_data.role.data
        team = grab_data.team.data
        department= user.department()   #   Department defined automatically
        
        if len(emp_name)*len(emp_surname)*len(role)*len(team) != 0 :

            MySQL.write(f"INSERT INTO employee(name, surname, position, team, department) VALUES('{emp_name}','{emp_surname}','{role}','{team}','{department}');")
            grab_data.emp_name.data = grab_data.emp_surname.data = grab_data.role.data = grab_data.team.data = ''

            msg = 'new employee added'
            
        else:
            msg = 'Please fill in the required fields'

    return render_template('nemployee.html', title='New employee', form=grab_data, message=msg, user=user)


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():

    grab_data = new_expense()

    if request.method=='POST':

        nature = grab_data.nature.data
        vendor = grab_data.vendor.data
        reason = grab_data.reason.data


    return render_template('expenses.html', title='Expenses page', form=grab_data, user=user)        


@app.route('/sales')
def sales():

    list=MySQL.get('SELECT * from client;')

    return render_template('dpt-sales.html', title='Sales', user=user, list=list)

@app.route('/HR', methods=['GET', 'POST'])
def HR():

    list=[]

    if request.method in ['GET', 'POST']:

        z=MySQL.get('SELECT * from HR;')
        list=z

    return render_template('dpt-hr.html', title='Human Resources', user=user, list=list)


"""     Here the app runs       and lives       not to touch        leave alone     logic above
"""


if __name__=='__main__':
    app.run(debug=True)

MySQL.off()