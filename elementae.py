usuarios = {'Daniel':'Sales', 'John':'HR', 'Jack':'Sales', 'Wesley':'HR'}
import pymysql

class Usuarium():

    def __init__(self):
        self.nm=[]
        self.dpt=[]

        
    def check(self, login, passwd):

        if login in usuarios:

            department = usuarios[login]
            self.nm.append(login)
            self.dpt.append(department)

            return True

    def name(self):
        return self.nm[len(self.nm)-1]

    def department(self):
        return self.dpt[len(self.dpt)-1]


class DanSQL():

    def __init__(self):

        self.Make = pymysql.connect(host='127.0.0.1', user='root', passwd='Buddhassister22', db='main')
        self.MySQL = self.Make.cursor()

    def sudo(self):

        self.Make.commit()

    def write(self, str):

        self.MySQL.execute(str)

    def off(self):
       
        self.Make.close()
        self.MySQL.close()


