import pytest
import pymysql



"""
This function will checks whether this table exists (table_name being the table)
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
