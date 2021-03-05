import pytest
import pymysql



"""
This function will checks whether this table exists (table_name being the table)
by returning True if it finds it or False if it doesn't

                                        // we can recycle it for multiple tests
"""

def TestDB(table_name):            

    Make=pymysql.connect(host='34.121.192.21', user='root', passwd='645202398', db='main')
    MySQL=Make.cursor()

    MySQL.execute('show tables;')     #     Connects with the MySQL DB, 
    tables = MySQL.fetchall()               
                                #           extracts a list of all tables
    
    for i in tables:                  #     and checks if our table is there yet

        if table_name in str(i):       return True      
        else:                       return False
    

def test():
    assert TestDB('table1') == True

def test1():
    assert TestDB('house') == True

def test2():
    assert TestDB('table2') == True

def test3():
    assert TestDB('table3') == True

def test4():
    assert TestDB('table4') == True
