import math
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, money):
        if self.balance < money:
            print("not enough money")
        else:
            self.balance -= money
            print("now your balance: " + str(self.balance) + "kzt")
            
    def deposit(self, money):
        self.balance += money
        print("now your deposit: " + str(self.balance) + "kzt")
        
x = Bank("Togzhan", 5000)
x.withdraw(2500)
x.deposit(3000)
x.withdraw(8000)

  
            