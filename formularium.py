from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField, FloatField, SelectField
from elementae import DanSQL, ListForm




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


class deales(FlaskForm):


    amount = StringField('Deal worth')
    client_id = SelectField('Who was the deal with ', choices=ListForm("SELECT company_name, id FROM client;", 'client'))
    employee_id = SelectField('Deal closed by ', choices=ListForm("SELECT name, surname, id FROM employee;", 'employee'))
    date = StringField('Date ')
    close_deal = SubmitField('Close deal')


class deleting(FlaskForm):

    many=[]
    pairing=dict()

    for i in DanSQL().get("SELECT date, amount, manager, details FROM HR;"):
        fname='£'+str(i[1])+' '+i[2]
        pairing[i[0]]=fname
    
    while (len(pairing)>0):
        many.append(pairing.popitem())

    action = SelectField('Action ', choices=[(1, 'View'), (2, 'Delete')])
    selection = SelectField('select ', choices = many)
    confirm = SubmitField('Confirm')


class deletings(FlaskForm):

    many=[]
    pairing=dict()

    for i in DanSQL().get("SELECT date, amount FROM sales;"):
        fname='£'+str(i[1])+' | '+str(i[0])
        pairing[i[0]]=fname
    
    while (len(pairing)>0):
        many.append(pairing.popitem())

    action = SelectField('Action ', choices=[(1, 'View'), (2, 'Delete')])
    selection = SelectField('select ', choices = many)
    confirm = SubmitField('Confirm')



class selection(FlaskForm):


    selection = SelectField('select ', choices=[('U', 'Update'), ('N', 'New Entry')])
    pressa = SubmitField('Confirm')


class updating(FlaskForm):

    many=[]
    pairing=dict()


    for i in DanSQL().get("SELECT company_name, contact_name, id FROM client;"):
        fname=str(i[0])+' | '+str(i[1])
        pairing[i[2]]=fname
    
    while (len(pairing)>0):
        many.append(pairing.popitem())

    listing=[('company_name', 'Company'), ('contact_name', 'Contact'), ('contact_surname', 'Surname'), ('phone', 'Phone'), ('details', 'Details')]

    edit = StringField('Edit ')
    select = SelectField('What Client ', choices=many)
    narrow= SelectField('What field', choices=listing)
    press = SubmitField('Confirm')