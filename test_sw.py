from elementae import Usuarium, DanSQL
import pytest

class Testuser():

    def run(any):
        trial = Usuarium()
        start_value=len(trial.dpt)
        trial.check(any, 'QA123@')
        if len(trial.dpt) != 0:
            if len(trial.dpt) == start_value +1:
                return True

    def nombre(any):
        trial = Usuarium()
        start_value=len(trial.nm)
        trial.check(any, 'QA123@')
        if trial.name() == any:
            return True




class MyAlchemy():

    def connects():

        try:
            attempt = DanSQL()
            return True
        
        except: return False
               

    def creates(value):

        attempt = DanSQL()
        
        attempt.write('CREATE DATABASE IF NOT EXISTS testbase;')
        attempt.write('use testbase;')
        
        attempt.write('CREATE TABLE IF NOT EXISTS Test(column1 VARCHAR(10));')
        attempt.write(f'INSERT INTO test(column1) values({str(value)});')   
        
        var = attempt.get('SELECT * FROM testbase.test;')

        attempt.write('DROP DATABASE testbase;')

        return str(var)       




def test0():                            # Checks the efficiency of class Usuarium in taking user Daniel
    assert Testuser.run('Daniel') == True

def test1():                            # Checks the efficiency of class Usuarium in taking user Daniel
    assert Testuser.nombre('Daniel') == True

def test2():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.run('Wesley') == True

def test3():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.nombre('Wesley') == True

def test4():                            # Checks that the conection with the database is successful for the object
    assert MyAlchemy.connects() == True

def test5():                            # Checks that the object can interact with the database using an integer
    assert '127' in MyAlchemy().creates(127)

def test6():                            # Checks that the object can interact with the database using a string
    assert 'Dan' in MyAlchemy().creates("'Dan'")


        