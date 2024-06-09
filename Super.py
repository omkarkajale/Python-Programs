class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod  #we are not using any attribute thats why we used staticmethod
    def start():
        print('Car Start')
        
    @staticmethod
    def stop():
        print('Car Stop')
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
car1=ToyotaCar('ss','bb')
print(car1.type)
print(car1.name)
