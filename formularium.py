from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField







class verifyU(FlaskForm):

    login = StringField('Username: ')
    passwd= StringField('Password: ')
    submit= SubmitField('Log in')

class new_client(FlaskForm):

    comp_name = StringField('Company name ')
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

    nature = StringField('Nature of the expense ')
    vendor = StringField('Name of the vendor ')
    reason = StringField('Reason of the expense')
    add_expense = SubmitField('Add expense')




