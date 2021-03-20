usuarios = {'Daniel':'Sales', 'John':'HR', 'Jack':'Sales', 'Wesley':'HR', 'SupremeOverlord':'Master'}
import pymysql

class Usuarium():

    def __init__(self):

        self.nm=''
        self.dpt=''

        
    def check(self, login, passwd):

        clave='QA123@'

        if login in usuarios and passwd == clave:

            department = usuarios[login]
            DanSQL().write('CREATE TABLE IF NOT EXISTS log(date DATETIME, user VARCHAR(20), department VARCHAR(20));')
            DanSQL().write(f"INSERT INTO log(date, user, department) VALUES (now(), '{login}', '{department}');")
           
            return True

    def set(self):

        self.nm  = str(DanSQL().get('select user from log where date=(select max(date) from log);'))
        self.dpt = str(DanSQL().get('select department from log where date=(select max(date) from log);'))



    def name(self):
        
        try:
            return self.nm
        except Exception as e:
            out = str(e) + str(len(self.nm)) 
            return out
            

    def department(self):
        try:
            return self.dpt

        except Exception as e:
            out = str(e) + str(len(self.nm)) 
            return out
            


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
