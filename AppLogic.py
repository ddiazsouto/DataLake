
""" 
        Here we define classes and objects
        Nothing else

        Keeping code tidy

"""

from elementae import DanSQL




def process_client(grab_data):

        company_name = grab_data.company_name.data        #   Assigning value
        contact_name = grab_data.contact_name.data        #   to the variables    
        contact_surname = grab_data.contact_surname.data  #   internally
        phone = grab_data.phone.data                      #   so we can 
        details= grab_data.details.data                   #   manipulate them
                                                        # with posterior logic
        
        if len(contact_name)*len(company_name)*len(phone) != 0:

            DanSQL().injects(f"INSERT INTO client(company_name, contact_name, contact_surname, phone, details) VALUES('{company_name}','{contact_name}','{contact_surname}','{phone}','{details}');")
            
            grab_data.company_name.data = grab_data.contact_name.data = grab_data.contact_surname.data = ''
            grab_data.phone.data = grab_data.details.data = ''

            msg = 'New client added'

        else:
            msg='Please, fill in all required fields'
        
        return grab_data, msg





def navigating_client(editing):

        msg=''
        edit = editing.edit.data
        option_selected=editing.narrow.data
        chosen_client = editing.select.data

        if option_selected != None :

            DanSQL().write(f"UPDATE client SET {option_selected}='{edit}' Where id={chosen_client};")
            msg= f"{option_selected} updated successfully"

        return editing, msg






def identitydirect(user):


    takeme_to=''

    if  'Sales' in user.department() :
        takeme_to = 'dpt-sales.html'

    elif 'HR' in user.department():
        takeme_to = 'dpt-hr.html'
        
    elif 'Master' in user.department():
        takeme_to = 'master.html'

    else:
        takeme_to = 'login.html'
    
    return str(takeme_to)





def employee_logic(grab_data, user):

    emp_name = grab_data.emp_name.data
    emp_surname= grab_data.emp_surname.data
    role = grab_data.role.data
    team = grab_data.team.data
    department= user.department()   #   Department defined automatically
    
    if len(emp_name)*len(emp_surname)*len(role)*len(team) != 0 :

        DanSQL().write(f"INSERT INTO employee(name, surname, position, team, department) VALUES('{emp_name}','{emp_surname}','{role}','{team}','{department}');")
        grab_data.emp_name.data = grab_data.emp_surname.data = grab_data.role.data = grab_data.team.data = ''

        msg = 'new employee added'
        
    else:
        msg = 'Please fill in the required fields'

    return grab_data, msg


def fexpenses(grab_data, user):

    
    amount = grab_data.amount.data
    details = str(grab_data.details.data)
    expense_id = int(grab_data.nature.data)
    manager = user.name()


    if type(amount)==float and len(details) > 0:

        DanSQL().write(f"INSERT INTO HR(date, expense_id, amount, details, manager) values (now(), {expense_id}, {amount}, '{details}', '{manager}');")

        grab_data.details.data = ''
        msg = 'New expense added'

    else:
        msg = 'Please fill in the required fields with valid information'

    return grab_data, msg

def dealfunct(grab_data):

    try:
        amount  = float(grab_data.amount.data)
    except:
        amount = 0
           

    client_id   = int(grab_data.client_id.data)
    employee_id = int(grab_data.employee_id.data)
    msg=''

    if amount >0 :    
                
        DanSQL().write(f"insert into sales(date, client_id, employee_id, amount) values(now(), {client_id}, {employee_id}, {amount});")
        grab_data.amount.data =  ''
        msg = 'Deal added'

    else:
        msg = 'Please fill in the required fields with valid information'

    return grab_data, msg