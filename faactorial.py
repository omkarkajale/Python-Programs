
class Fact:
    def __init__(self,num=5,total=1):
        for i in range(2,num+1):
           total *= i
        print(total)
f=Fact()
            