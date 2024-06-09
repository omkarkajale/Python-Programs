''' class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no
bank=Account(12000,1234567)
print(bank.bal)
print(bank.acc_no)# Everyone can easily access the bank account information 
'''
class Account:
    def __init__ (self,acc_pass,acc_no):
        self.__acc_pass=acc_pass
        self.acc_no=acc_no  # it willl become an private 
    def reset_pass(self):
        print(self.__acc_pass)
bank=Account(12000,1234567)
#print(bank.__acc_no)  # it will give an errror if access ths from outside the class
print(bank.reset_pass())