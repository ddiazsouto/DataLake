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
from AppLogic import process_client, navigating_client, doublecheck

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

now = datetime.now()






@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():

    template='login.html'

    form = verifyU()
    msg=''

    if request.method=='POST' and user.check(form.login.data, form.passwd.data ) == True:

        template = doublecheck(user)  


    elif request.method=='POST':
            msg='Please, wrong username or password'


    return render_template(template, title='Log-in', form=form, message=msg, user=user)





@app.route('/add-client', methods=['GET', 'POST'])
def client():

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
    msg = ''

    if request.method=='POST' and user.department() == 'HR':   
        
        date = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        amount = float(grab_data.amount.data)
        details = str(grab_data.details.data)
        expense_id = int(grab_data.nature.data)
        manager = user.name()


        if amount*len(details) != 0:

            MySQL.write(f"INSERT INTO HR(date, expense_id, amount, details, manager) values (now(), {expense_id}, {amount}, '{details}', '{manager}');")

            grab_data.amount.data = 0.0
            grab_data.details.data = ''
            msg = 'New expense added'

        else:
            msg = 'Please fill in the fields with valid information'


    return render_template('expenses.html', title='Expenses page', form=grab_data, user=user, message=msg)        



@app.route('/deals', methods=['GET', 'POST'])
def deals():


    grab_data=deales() 
    msg=''

    if request.method=='POST':

        amount      = float(grab_data.amount.data)
        client_id   = int(grab_data.client_id.data)
        employee_id = int(grab_data.employee_id.data)
                
        MySQL.write(f"insert into sales(date, client_id, employee_id, amount) values(now(), {client_id}, {employee_id}, {amount});")
        grab_data.amount.data =  ''
        msg = 'Deal added'


                     

    return render_template('deals.html', title='Deals', user=user, form=grab_data, message=msg)



@app.route('/sales')
def sales():

    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from client;')

    return render_template('dpt-sales.html', title='Sales', user=user, list=list)




@app.route('/HR', methods=['GET', 'POST'])
def HR():

    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from HR;')
        

    return render_template('dpt-hr.html', title='Human Resources', user=user, list=list)





@app.route('/Over', methods=['GET', 'POST'])
def Master():

        #    Missing some logic here

    return render_template('master.html', title='Master', user=user)





@app.route('/master-HR', methods=['GET', 'POST'])
def MasterHR():

    grab_data = deleting()
    msg='Dan'
    list=[]

    if request.method=='GET':
        list=MySQL.get('SELECT * from HR;')
    
    if request.method == 'POST':

        action = grab_data.action.data
        selection = grab_data.selection.data

        msg=f'Not Dan, POST{action}, {selection}'

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