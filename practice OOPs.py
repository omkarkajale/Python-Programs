class Account:
    def __init__(self,bal,acc):
        self.balance =bal
        self.account_no=acc 
    def debit(self,amount):
        self.balance -= amount
        print("RS.",amount,"from Your account","Was Debited")
        print("Total Balance =",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("RS.",amount,"from Your account ","is Credited")
        print("Total balance =",self.get_balance())
    def get_balance(self):
        return self.balance
        
bank=Account(10000,23456)
bank.debit(1000)
bank.credit(500)