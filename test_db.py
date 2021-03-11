import pytest
import pymysql
from flask_testing import TestCase
from flask import url_for

from app import app, db
from tables import Expenses, Sales, Employee, HR, Client


"""
This function will check whether this table exists (table_name being the table) in MySQL
by returning True if it finds it or False if it doesn't

                                        // we can recycle it for multiple tests
"""

def TestDB(Tn):            

    Make=pymysql.connect(host='34.121.192.21', user='root', passwd='645202398', db='main')
    MySQL=Make.cursor()

    MySQL.execute('show tables;')     #     Connects with the MySQL DB, 
    tables = MySQL.fetchall()               
                                #           extracts a list of all tables
    
    for i in tables:                  #     and checks if our table is there yet

        if str(Tn) in str(i):       
                                                                                                                #print('passed', type(Tn), type(i), f'{Tn} and {i} are equal? ', Tn in str(i))
            return True

        else:                       
                                                                                                                #print(type(Tn), type(i), f'{Tn} and {i} are equal? ', Tn in str(i))
            continue

    #           Now we call those functions to check whether the databases exist
def test():
    assert TestDB('sales') == True

def test1():
    assert TestDB('HR') == True

def test2():
    assert TestDB('employee') == True

def test3():
    assert TestDB('client') == True

def test4():
    assert TestDB('xpense') == True


"""
The previous tests are not increasing coverage, because they don't test code but the MySQL tables
We will need flask-testing to get the coverage, however, we leave those functions for extra testing
"""

class TestBase(TestCase):   # main function to create the app environment

    def create_app(self):   # its configuration

            app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='DANs_TESTING_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False )
            
            return app

    def setUp(self):    # and initialising it

        db.create_all()

        #Entry2 = Client

    def tearDown(self): # after closing

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):  # This test confirms that the page loads

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        

# Test ready for employee formulary

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name='Dan', surname='Souto', position='Trainee', team='Dara\'s', department='DevOps'),
         
            follow_redirects=True
        )
        #self.assertIn(b'Dan',response.data)
