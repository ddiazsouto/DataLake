# External modules
import pymysql
from datetime import datetime
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
# Those were the external modules 

# Internal modules:
from formularium import verifyU, new_client, new_employee, new_expense, deales, deleting, deletings, selection, updating

from elementae import Usuarium, DanSQL
from AppLogic import process_client, navigating_client, identitydirect, employee_logic, fexpenses, dealfunct

# Those were the internal modules


"""
Up here the app and database configuration are defined as well as their connections to python

First the connection the database through SQLAlchemy

"""


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'   
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Buddhassister22@127.0.0.1/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'


db=SQLAlchemy(app)



"""
Now some logic for the app and its routes

"""


user = Usuarium()                         # We create an object to control the user login

MySQL=DanSQL()

now = datetime.now()






@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():

    user = Usuarium()
    

    template='login.html'

    form = verifyU()
    msg=''

    if request.method=='POST' and user.check(form.login.data, form.passwd.data ) == True:
        user.set()
        template = identitydirect(user)                         #   Confirms the user and directs us
#                                                                  to the right template
    elif request.method=='POST':
            msg='Please, wrong username or password'


    return render_template(template, title='Log-in', form=form, message=msg, user=user)





@app.route('/add-client', methods=['GET', 'POST'])
def client():

    user=Usuarium()
    user.set()

    grab_data = new_client()
    grab = selection()
    editing=updating()
    msg=''
    

    if request.method=='POST':

        grab_data, msg = process_client(grab_data)         
        editing, msg = navigating_client(editing)


    return render_template('client.html', form3=editing, message=msg, form1=grab, form=grab_data, user=user)



@app.route('/new-employee', methods=['GET', 'POST'])
def nemployee():

    user=Usuarium()
    user.set()

    grab_data = new_employee()
    msg =''

    if request.method=='POST':        
        grab_data, mmsg = employee_logic(grab_data, user)

    return render_template('nemployee.html', title='New employee', form=grab_data, message=msg, user=user)



@app.route('/expenses', methods=['GET', 'POST'])
def expenses():

    user=Usuarium()
    user.set()

    grab_data = new_expense()
    msg = ''

    if request.method=='POST' and user.department() == 'HR':   

        grab_data, msg = fexpenses(grab_data, user)    



    return render_template('expenses.html', title='Expenses page', form=grab_data, user=user, message=msg)        



@app.route('/deals', methods=['GET', 'POST'])
def deals():

    user=Usuarium()
    user.set()

    grab_data=deales() 
    msg=''

    if request.method=='POST':
        grab_data, msg = dealfunct(grab_data)                     

    return render_template('deals.html', title='Deals', user=user, form=grab_data, message=msg)




@app.route('/sales')
def sales():

    user=Usuarium()
    user.set()

    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from client;')

    return render_template('dpt-sales.html', title='Sales', user=user, list=list)




@app.route('/HR', methods=['GET', 'POST'])
def HR():

    user=Usuarium()
    user.set()

    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from HR;')
        

    return render_template('dpt-hr.html', title='Human Resources', user=user, list=list)





@app.route('/Over', methods=['GET', 'POST'])
def Master():

    user=Usuarium()
    user.set()

        #    Missing some logic here

    return render_template('master.html', title='Master', user=user)





@app.route('/master-HR', methods=['GET', 'POST'])
def MasterHR():

    user=Usuarium()
    user.set()

    grab_data = deleting()
    msg='Dan'
    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from HR;')
    
    if request.method == 'POST':

        action = grab_data.action.data
        selection = grab_data.selection.data

        msg=''

        if int(action) == 1:
            list=MySQL.get(f"SELECT * from HR WHERE date='{selection}';")   
            msg = 'This is what you selected'     
            return render_template('masterhr.html', title='HR edit', form=grab_data, list=list, user=user, message=msg)

        elif int(action) == 2:
            MySQL.write(f"DELETE from HR WHERE date='{selection}';")
            msg = 'Entry deleted' 


    return render_template('masterhr.html', title='HR edit', form=grab_data, list=list, user=user, message=msg)




@app.route('/master-sales', methods=['GET', 'POST'])
def Mastersales():

    user=Usuarium()
    user.set()

    grab_data = deletings()
    msg='Dan'
    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from sales;')
    
    if request.method == 'POST':

        action = grab_data.action.data
        selection = grab_data.selection.data

        msg=''

        if int(action) == 1:
            list=MySQL.get(f"SELECT * from sales WHERE date='{selection}';")   
            msg =f'Not Dan, POST{action}, {selection}'    
            return render_template('mastersales.html', title='HR edit', form=grab_data, list=list, user=user, message=msg)

        elif int(action) == 2:
            MySQL.write(f"DELETE from sales WHERE date='{selection}';")
            msg = 'Enty deleted successfully' 


    return render_template('mastersales.html', title='HR edit', form=grab_data, list=list, user=user, message=msg)




"""     Here the app runs       and lives       not to touch        leave alone     logic above
"""


if __name__=='__main__':
    app.run(debug=True)

MySQL.off()