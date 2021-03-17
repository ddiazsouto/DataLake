from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField, FloatField, SelectField
from elementae import DanSQL




class verifyU(FlaskForm):

    login = StringField('Username: ')
    passwd= StringField('Password: ')
    submit= SubmitField('Log in')

class new_client(FlaskForm):

    company_name = StringField('Company name ')
    contact_name= StringField('Name of the person in contact ')
    contact_surname = StringField('Surname of the person in contact ')
    phone = StringField('Phone number ')
    details = StringField('Introduce client details ')
    add_client = SubmitField('Add Client ')

class new_employee(FlaskForm):

    emp_name = StringField('New employee name ')
    emp_surname= StringField('New employee Surname ')
    role = StringField('Role ')
    team = StringField('Team ')
    department= StringField('Department ')
    add_employee = SubmitField('Add employee')

class new_expense(FlaskForm):

    
    pairing=dict()
    for i in DanSQL().get("select * from expenses;"):
        nature=i[1]+'-'+i[2]
        pairing[i[0]]=nature

    many=[]
    while (len(pairing)>0):
        many.append(pairing.popitem())
    

    date = StringField('Date ')
    amount = FloatField('How much ')
    nature = SelectField('Nature of the expense', choices=many)
    details = StringField('Reason of the expense')
    manager= StringField('Manager')
    add_expense = SubmitField('Add expense')





