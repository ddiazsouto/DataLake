from elementae import unscape, Usuarium, DanSQL, usuarios
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
        attempt.write(f'INSERT INTO Test(column1) values({str(value)});')        
        var = attempt.get('SELECT * FROM testbase.Test;')
        attempt.write('DROP DATABASE testbase;')

        return str(var)    


# class sqlLists():

#     def __init__(self):

#         attempt = DanSQL






def test0():                            # Checks the efficiency of class Usuarium logging the testing
    assert Testuser.runcheck('Test') == True

def test1():                            # Checks the efficiency of class Usuarium in taking user Daniel
    assert Testuser.runcheck('Daniel') == True

def test2():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.runcheck('Wesley') == True

def test3():                            # Checks the efficiency of class Usuarium in taking user Wesley
    assert Testuser.retain() == True

def test4():                            # Checks that the conection with the database is successful for the object
    assert MyAlchemy.connects() == True

def test5():                            # Checks that the object can interact with the database using an integer
    assert '127' in MyAlchemy.creates(127)

def test6():                            # Checks that the object can interact with the database using a string
    assert 'Dan' in MyAlchemy.creates("'Dan'")

def test7():
    assert unscape("(('Daniel',),)") == 'Daniel'

def test8():
    assert unscape("(('HR',),)") == 'HR'




        