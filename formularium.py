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
    
    print(many)
    date = StringField('Date ')
    amount = FloatField('How much ')
    nature = SelectField('Nature of the expense', choices=many)
    details = StringField('Reason of the expense')
    manager= StringField('Manager')
    add_expense = SubmitField('Add expense')


class deales(FlaskForm):

    many=[[], []]
    pairing1=dict()
    pairing2=dict()

    for i in DanSQL().get("SELECT company_name, id FROM client;"):
        nature=i[1]
        pairing1[nature]=i[0]

    for i in DanSQL().get("SELECT name, surname, id FROM employee;"):
        fname=i[0]+' '+i[1]
        pairing2[i[2]]=fname
    
    while (len(pairing1)>0):
        many[0].append(pairing1.popitem())

    while (len(pairing2)>0):
        many[1].append(pairing2.popitem())

    print(many[0], '\n', many[1])

    amount = StringField('Deal worth')
    client_id = SelectField('Who was the deal with ', choices=many[0])
    employee_id = SelectField('Deal closed by ', choices=many[1])
    date = StringField('Date ')
    close_deal = SubmitField('Close deal')


