
class person:
    __person ='user'
    def __init__(self):
        print(self.__person)
    def __name(self):       # prive function
        print('hello person')
    def welcome(self):  # call function
        self.__name()
dd=person()
print(dd.welcome())
# print(dd.__person) it will throw an error
#print(dd.__name())