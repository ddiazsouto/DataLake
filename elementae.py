usuarios = {'Daniel':'Sales', 'John':'HR', 'Jack':'Sales', 'Wesley':'HR', 'SupremeOverlord':'Master'}
import pymysql

class Usuarium():

    def __init__(self):
        self.nm=[]
        self.dpt=[]

        
    def check(self, login, passwd):

        clave='QA123@'

        if login in usuarios and passwd == clave:

            self.nm=[]
            self.dpt = []

            department = usuarios[login]
            self.nm.append(login)
            self.dpt.append(department)

            return True

    def name(self):
        try:
            return self.nm[0]
        except: return None
            

    def department(self):
        try:
            return self.dpt[0]
        except: return None
            


class DanSQL():

    def __init__(self):

        self.Make = pymysql.connect(host='34.121.192.21', user='root', passwd='645202398', db='main')
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
        out = init.MySQL.fetchall()
        init.off()
        return out

    def off(self):
       
        self.Make.close()
        self.MySQL.close()


class ListForm():

    def __init__(self):

        self.many=[]
        self.pairing=dict()

    def employee(self, stringin):

        for i in DanSQL().get(stringin):
            fname=i[0]+' '+i[1]
            self.pairing[i[2]]=fname
                
        while (len(self.pairing)>0):
            self.many.append(self.pairing.popitem())

        return self.many


    def client(self, stringin):

        for i in DanSQL().get(stringin):
            nature=i[1]
            self.pairing[nature]=i[0]
        
        while (len(self.pairing)>0):
            self.many.append(self.pairing.popitem())

        return self.many