
""" 
        Here we define classes and objects
        Nothing else

        Keeping code tidy

"""

from elementae import DanSQL

class student:
    
    def __init__(self, name, age, class_):
        
        self.name=name
        self.age=age
        self.class_=class_
        
        
    def avg3(self, score1, score2, score3):
        calc=(score1+score2+score3)/3
        print(calc)
        
    
# getattr()
# hasattr()
# setattr()
        
        
        
class stud:
    
    def __init__(self):
        
        self.name=''
        self.age=''
        self.class_=[]
        self.score=[]
        self.map={}
        
    def avg(self):
        
        j=int(input('how many exams do you want to add? '))
        for i in range(j):
            subj=input(f'What Subject was the exam number {i+1} about? ')
            a=input(f'{subj} exam score: ')
            self.score.append(int(a))
            self.class_.append(subj)
        
        print('\n\nThe mean of all scores is: ', end='')
        print(sum(self.score)/len(self.score))
        
    def describe(self):
        
        print(f'Name: {self.name} \nSubjets: {set(self.class_)} \nScores so far: {self.score}')
        
    
    def compress(self):
        
               
        for i, j in zip(self.class_, self.score):
            
            q1=i
            q2=j
            answer=[q1, q2]
            if q1 in self.map:
                self.map[q1].append(q2)
            elif q1 not in self.map:
                self.map[q1]=[q2]
            else:
                print('WTF is this dude?')
                
            self.class_=[]
            self.score=[]
        

class alumn(stud):
    def __init__(self, name):
        super(alumn, self).__init__()
        
        self.name=name



def processc(grab_data):

        company_name = grab_data.company_name.data        #   Assigning value
        contact_name = grab_data.contact_name.data        #   to the variables    
        contact_surname = grab_data.contact_surname.data  #   internally
        phone = grab_data.phone.data                      #   so we can 
        details= grab_data.details.data                   #   manipulate them
                                                        # with posterior logic
        
        if len(contact_name)*len(company_name)*len(phone) != 0:

            DanSQL().injects(f"INSERT INTO client(company_name, contact_name, contact_surname, phone, details) VALUES('{company_name}','{contact_name}','{contact_surname}','{phone}','{details}');")
            
            grab_data.company_name.data = grab_data.contact_name.data = grab_data.contact_surname.data = ''
            grab_data.phone.data = grab_data.details.data = ''

            msg = 'New client added'

        else:
            msg='Please, fill in all required fields'
        
        return grab_data, msg