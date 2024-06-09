class EvenOdd:
    def __init__(self,num):
        self.num=num
        if (self.num % 2==0): 
            print(self.num,'is Even number')
       
        else:
            print(self.num,'is Odd number')
num=int(input('Enter number'))
EvenOdd(num)