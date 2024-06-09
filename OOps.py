'''class person:
    name="John"
f=person()
print(f.name)'''

'''class person:
    name="John"
    def rename(self,name):
        self.name=name
f=person()
f.rename('Sanjana Omkar Kajale')
print(f.name)
print(person.name)  #this is one of the way to change class(person) attribute
'''
'''class person:
    name="John"
    def rename(self,name):
        person.name=name # class name 
f=person()
f.rename('Sanjana Omkar Kajale')
print(f.name)
print(person.name)'''

'''
class person:
    name="John"
    def rename(self,name):
        self.__class__.name='Rahul'    # We are accessing the class
f=person()
f.rename('Sanjana Omkar Kajale')
print(f.name)
print(person.name) '''

class person:
    name="John"
    @classmethod # is an decorator
    def changeName(cls,name):  # it will directly change the class attribute
        cls.name=name
f=person()
f.changeName('leo')
print(f.name)
print(person.name)

