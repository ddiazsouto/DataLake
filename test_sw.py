from elementae import unscape, Usuarium, usuarios
import pytest



class Testuser():

    def runcheck( any):
        trial = Usuarium()                  # Here we test that out object does the job checking the user
        return trial.check(any, 'QA123@')   #        in the login menu
        

    def retain():
        trial = Usuarium()                          # here we test that the object works as desired,
        if trial.nm == '' and trial.dpt == '':     #  that it initialises as an empty string
            
            trial.set()                          # that it activates the object with the active user

            return len(trial.nm) > 1 and len(trial.dpt) > 1     # and that it retains information correctly







def test0():                            # Checks the efficiency of class Usuarium logging the testing
    assert Testuser.runcheck('Test') == True

def test1():                            # Checks the efficiency of class Usuarium in taking user Daniel
    assert Testuser.runcheck('Daniel') == True

def test2():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.runcheck('Wesley') == True

def test3():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.retain() == True



"""
Here we test our Database interactive Object
"""

from elementae import DanSQL



class MyAlchemy():

    def connects():

        try:
            attempt = DanSQL()
            attempt.off()
            return True
        
        except: return False
               

    def creates(value):

                
        DanSQL().write('CREATE DATABASE IF NOT EXISTS testbase;')
        DanSQL().write('USE testbase;')        
        DanSQL().write('CREATE TABLE IF NOT EXISTS Test(column1 VARCHAR(10));')
        DanSQL().write(f'INSERT INTO Test(column1) values({str(value)});')        
        var = DanSQL().get('SELECT * FROM Test;')
        DanSQL().write('DROP DATABASE testbase;')

        

        return str(var)    


# class sqlLists():

#     def __init__(self):

#         attempt = DanSQL






def test4():                            # Is the conection with the database successful ?
    assert MyAlchemy.connects() == True

def test5():                            # Checks that the object can interact with the database using an integer
    assert '127' in MyAlchemy.creates(127)

def test6():                            # Checks that the object can interact with the database using a string
    assert 'Dan' in MyAlchemy.creates("'Dan'")

def test7():
    assert unscape("(('Daniel',),)") == 'Daniel'

def test8():
    assert unscape("(('HR',),)") == 'HR'



"""
Here we test the AppLogic module
"""

from AppLogic import identitydirect, process_client
from formularium import verifyU, new_client
from test_db import TestBase
from flask import url_for
from app import app


def RedirectLogic(user_dpt):

    attempt = Usuarium()
    attempt.dpt = user_dpt                # we modify the department directly

    return identitydirect(attempt)        # This method takes in a Usuarium object 

    #                                                from 'elementae' module

class LogicInteract(TestBase):

    def test_add_post(self):
        response = self.client.post(
            url_for('login'),
            data = dict(login='Daniel', passwd='QA123'),
         
            follow_redirects=True
        )


    def test_add_post0(self):              # Checks that the page is stable

        response = self.client.post(       #  in /add-client, both
            url_for('client'),
            data = dict(selection='U',     #     Updating
                edit='Any text'),                   
            follow_redirects=True
        )             
        response = self.client.post(       #   And adding a 
            url_for('client'),
            data = dict(selection='N',      #   new entry
                edit='Any text'),                   
            follow_redirects=True
        )


    def test_add_post1(self):               # This has SelectField
        response = self.client.post(
            url_for('expenses'),
            data = dict(amount=50.05, details='Reason of the expense'),         
            follow_redirects=True
        )
      
      
    
    def test_add_post2(self):
        response = self.client.post(
            url_for('nemployee'),
            data = dict(name='Dan', surname='Souto', position='Trainee', team='Dara\'s', department='DevOps'),         
            follow_redirects=True   # Tests the page with form /new-employee
        )

      
    def test_add_post3(self):               #This has SelectField
        response = self.client.post(
            url_for('deals'),
            data = dict(amount=1234, client_id=5, employee_id=5),         
            follow_redirects=True   # Tests the page /deals
        )

    def test_add_post4(self):               #This has SelectField
        response = self.client.post(
            url_for('what'),
            data = dict(action=1, selection='2021-03-21 15:05:36'),         
            follow_redirects=True   # Tests the page /deals
        )

        response = self.client.post(
            url_for('what'),
            data = dict(action=2, selection='2021-03-21 15:05:36'),         
            follow_redirects=True   # Tests the page /deals
        )

    def test_add_post5(self):               #This has SelectField
        response = self.client.post(
            url_for('Mastersales'),
            data = dict(action=1, selection='2021-03-21 15:05:36'),         
            follow_redirects=True   # Tests the page /deals
        )

        response = self.client.post(
            url_for('Mastersales'),
            data = dict(action=2, selection='2021-03-21 15:05:36'),         
            follow_redirects=True   # Tests the page /deals
        )




"""
Testing the logic in code for AppLogic

"""






def test9():
    assert RedirectLogic('Sales') == 'dpt-sales.html'    # Does the logic take us to the right template?

def test10():
    assert RedirectLogic('HR') == 'dpt-hr.html' 

def test11():
    assert RedirectLogic('Master') == 'master.html' 

def test12():
    assert RedirectLogic('testeator') == 'login.html' 

# def test13():
#     assert TestProcessClient ('QA Ltd','Daniel','Diaz Souto','647897997','') != ''