'''
class Student:
    def __init__(self,phy,chem,math):
        self.phy =phy
        self.chem =chem
        self.math =math
        self.percentage=str((self.phy+self.chem+self.math) /3 ) + "%"
stu1=Student(89,78,98)
print(stu1.percentage) # percentage of student
stu1.phy=97
print(stu1.phy)
print(stu1.percentage) #it will not change the percentage'''

class Student:
    def __init__(self,phy,chem,math):
        self.phy =phy
        self.chem =chem
        self.math =math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math) /3 ) + "%" # it will chnage the percentage
stu1=Student(89,78,98)
print(stu1.percentage) # percentage of student
stu1.phy=97
print(stu1.percentage) #it will not change the percentage