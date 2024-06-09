'''class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return (22/7) * self.radius ** 2
    def Parimeter(self):
        return 2*(22/7) * self.radius
Sol=Circle(21)
print(Sol.Area())
print(Sol.Parimeter())'''
'''
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.salary=salary
        self.dept=dept
    def show(self):
        print(self.role,self.dept,self.salary)
        
class Engineer(Employee):
    def __init__(self,age,name):
        self.age=age
        self.name=name
        super().__init__('Software Engineer','Developer','56000')
        print(self.age,self.name)
eng1=Engineer(22,'Omkar')
print(eng1.show())
'''

class Order:
    def __init__(self,price,item):
        self.price=price
        self.item=item
    def __gt__(self,odr2):
        return self.price > odr2.price
odr1=Order(12,'chiwda')
odr2=Order(23,'chips')
print(odr1>odr2) # we will get false bcz odr1 is smaall the odr2

