from elementae import Usuarium, DanSQL
import pytest

def Testuser(any):

    
    trial = Usuarium()
    start_value=len(trial.dpt)
    trial.check(any, 'QA123@')
    if len(trial.dpt) != 0:
        if len(trial.dpt) == start_value +1:
            return True




class MyAlchemy():


    def connects():

        try:
            attempt = DanSQL()
            return True
        
        except:
            return False

    

    def creates(value):

        attempt = DanSQL()
        
        attempt.write('CREATE DATABASE testbase')
        attempt.write('use testbase')
        attempt.write('CREATE TABLE Test(column1 VARCHAR(10));')
        attempt.write(f'INSERT INTO test(column1) values({str(value)});')   
        
        var = attempt.get('SELECT * FROM test;')
        attempt.write('DROP DATABASE testbase;')

        return str(var)       


def test1():                            # Checks the efficiency of class Usuarium in taking user Daniel
    assert Testuser('Daniel') == True

def test2():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser('Wesley') == True

def test3():                            # Checks that the conection with the database is successful for the object
    assert MyAlchemy.connects() == True

def test4():                            # Checks that the object can interact with the database
    assert '127' in MyAlchemy.creates(127)




        