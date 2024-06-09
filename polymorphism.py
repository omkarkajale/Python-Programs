'''
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNumbers(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,num2):
        newReal = self.real + num2.real
        newImg=self.img + num2.img
        return complex(newReal ,newImg)
        
num1=complex(12,32)
num1.showNumbers()
num2=complex(11,2)
num2.showNumbers()
num3=num1.add(num2)
num3.showNumbers() '''

'''
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNumbers(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,num2):
        newReal = self.real + num2.real
        newImg=self.img + num2.img
        return complex(newReal ,newImg)
        
num1=complex(12,32)
num1.showNumbers()
num2=complex(11,2)
num2.showNumbers()
num3=num1.add(num2)
num3.showNumbers() 
'''

class complex:
    def __init__(self,real,img):  # this also and dunder fun
        self.real=real
        self.img=img
    
    def showNumbers(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):   #dendudder function for + add   and Operator Overloading
        newReal = self.real + num2.real
        newImg=self.img + num2.img
        return complex(newReal ,newImg)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg=self.img - num2.img
        return complex(newReal ,newImg)
        
num1=complex(12,32)
num1.showNumbers()
num2=complex(11,2)
num2.showNumbers()
num3=num1-num2
num3.showNumbers() 