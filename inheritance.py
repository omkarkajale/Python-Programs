class Car:
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("stop")
class Car_Company(Car):   # inheritance  type Single Inheritance
    def __init__(self,car_name):
        self.car_name=car_name
        print("Car Name =",self.car_name)
car1=Car_Company('Kia')
car2=Car_Company('Swift')
print(car1.start())
        