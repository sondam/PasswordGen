'''
Created on Apr 19, 2017

@author: sonal
'''
import unittest
from PasswordGenerator import PasswordGeneratorClass 

plength = input("Specify length ")
password = PasswordGeneratorClass(plength)
#print (type(password.returnPassword() ))

print ("password is "+ ''.join(str(e) for e in password.returnPassword()))     

   
class CheckPasswordRequirements(unittest.TestCase):
    
    
    def test_size(self):
        
        self.assertEqual(len(password.returnPassword()), int(plength),"Password size incorrect")
        
    def test_isupper(self):
        count = 0
        for l in password.returnPassword():
            if (l.isupper()):
                count =+ 1
            else:
                pass
        self.assertEqual(count, 1, "Password does not contains uppercase letter")    
                
    def test_islower(self):
        count = 0
        for l in password.returnPassword():
            if (l.islower()):
                count =+ 1
            else:
                pass
        self.assertEqual(count, 1, "Password does not contains lowercase letter")    
                    
    def test_specialCharacter(self):
        for l in password.returnPassword():
            if (l in PasswordGeneratorClass.specialSeq):
                count =+ 1
            else:
                pass
        self.assertEqual(count, 1, "Password does not contains special character ")
            
if __name__ == '__main__':
    unittest.main()



