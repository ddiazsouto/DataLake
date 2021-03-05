import pytest
import pymysql





def TestDB(table_name):

    Make=pymysql.connect(host='34.121.192.21', user='root', passwd='645202398', db='main')
    MySQL=Make.cursor()

    MySQL.execute('show tables;')
    tables = MySQL.fetchall()

    
    for i in tables:    

        if table_name in str(i):       return True      
        else:                       return False
    





def test():

    assert TestDB()==True

