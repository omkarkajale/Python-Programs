class Car:
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("stop")
class Car_Company(Car):   # inheritance  type Multilevel Inheritance
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Car_Company):# inherit the Car_Company
    def __init__(self,type):
        self.type=type
car1=Fortuner('Ev')  # it calls the first class Car
car1.start()