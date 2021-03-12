usuarios = {'Daniel':'Sales', 'John':'HR', 'Jack':'Sales', 'Wesley':'HR'}

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


