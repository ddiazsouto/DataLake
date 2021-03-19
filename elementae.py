usuarios = {'Daniel':'Sales', 'John':'HR', 'Jack':'Sales', 'Wesley':'HR', 'SupremeOverlord':'Master'}
import pymysql

class Usuarium():

    def __init__(self):
        self.nm=[]
        self.dpt=[]

        
    def check(self, login, passwd):

        clave='QA123@'

        if login in usuarios and passwd == clave:

            department = usuarios[login]
            self.nm.append(login)
            self.dpt.append(department)

            return True

    def name(self):
        try:
            return self.nm[len(self.nm)-1]
        except: return None
            

    def department(self):
        try:
            return self.dpt[len(self.dpt)-1]
        except: return None
            


class DanSQL():

    def __init__(self):

        self.Make = pymysql.connect(host='127.0.0.1', user='root', passwd='Buddhassister22', db='main')
        self.MySQL = self.Make.cursor()

    def sudo(self):

        self.Make.commit()

    def write(self, str):

        self.MySQL.execute(str)
        self.sudo()

    def injects(self, str):

        init=DanSQL()

        init.MySQL.execute(str)
        init.sudo()
        init.off()

    def get(self, str):

        init=DanSQL()

        init.MySQL.execute(str)
        return init.MySQL.fetchall()

    def off(self):
       
        self.Make.close()
        self.MySQL.close()


