
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField


from formularium import verifyU, new_client, new_employee, new_expense
from elementae import Usuarium

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'    ---->>> Original (this one goes to production and to the cloud)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Buddhassister22@127.0.0.1/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dAnIel52'

db=SQLAlchemy(app)




# Up until here we deal with the database and the app object,
#  we need it clear and isolated because we are using it in other files

"""
Now some logic for the app and dfining objects
"""


user = Usuarium()








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
                return render_template('dpt-hr.html', form=form, title='HR', name=user.name(), department=user.department())


        else:
            msg='Please, that is a wrong username'

    return render_template('login.html', title='Log-in', form=form, message=msg)





@app.route('/add-client', methods=['GET', 'POST'])
def sales():

    grab_data = new_client()
    msg=''

    if request.method=='POST':

        
        company_name = grab_data.company_name.data  #   Assigning value
        contact_name = grab_data.contact_name.data  #   to the variables    
        contact_surname = grab_data.contact_surname.data    #   internally
        phone = grab_data.phone.data                    #   so we can 
        details= grab_data.details.data             #   manipulate them
                                                 # with posterior logic

        if len(contact_name)*len(company_name)*len(phone) != 0:
            # new_entry=Client(company_name=company_name, contact_name=contact_name, phone=phone )
            # db.session.add(new_entry)
            return render_template('client.html', title='New Client', message=msg, form=grab_data)

        else:
            msg='Please, fill in all required fields'


    return render_template('client.html', title='New Client', message=msg,  form=grab_data)



@app.route('/new-employee', methods=['GET', 'POST'])
def nemployee():

    grab_data = new_employee()


    if request.method=='POST':
        
        emp_name = grab_data.emp_name.data
        emp_surname= grab_data.emp_surname.data
        role = grab_data.role.data
        team = grab_data.team.data
        department= grab_data.department.data

        # Missing logic here
        

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
