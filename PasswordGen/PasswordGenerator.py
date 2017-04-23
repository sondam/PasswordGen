'''
Created on Apr 19, 2017

@author: sonal
'''
import random
import string
from builtins import dict, range
class PasswordGeneratorClass:
    specialSeq = ['@', '$','&']
    password = []
    def __init__(self, passlength):
        self.passwordlength = passlength
        
        num2alpha = dict(zip(range(1,26),string.ascii_lowercase))
        num2ALPHA = dict(zip(range(1,26),string.ascii_uppercase))
        randPlace1 = random.randrange(int(passlength)) # place special character here
        
        randRang = list(range(1, int(passlength))) #random place for capital alphabet
        
        randRang.remove(randPlace1)
       
        randPlace2 = random.choice(randRang) # place where capital alphabet can be placed
        
        for i in range(1,int(passlength)): 
            if (i == randPlace1):
                self.password.append(random.choice(PasswordGeneratorClass.specialSeq)) #print (random.choice(seq))
            if (i == randPlace2):
                self.password.append(num2ALPHA[random.randrange(1,26)]) #print (num2ALPHA[random.randrange(1,26)])    
            else:
                self.password.append(num2alpha[random.randrange(1,26)]) #print (num2alpha[random.randrange(1,26)])
        
    def returnPassword(self):
        return self.password    
