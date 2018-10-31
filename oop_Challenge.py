class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

        print("Owner:  {}".format(self.owner))
        print("Balance:  {}".format(self.balance))
    
    def deposit(self, amount):
        self.balance += amount 
        return "Your actual balance is: {}".format(self.balance)
        
    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            return "Your actual balance is: {}".format(self.balance)
        else:
            return "Funds Unavailable!"

acct1 = Account('Jose',100)
print(acct1.deposit(1100))
print("--------------")
print(acct1.withdraw(1500))

