# ENCAPSULATION EXAMPLE
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" you deposided {amount} ✅")
        else:
            print("deposit must be Positive")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successful ✅ \n Withdraw {amount} ")
        else:
            print("Insufficient funds ⚠️")

    def get_Balance(self):
        return self.__balance
    
myAccount = BankAccount(1234, 5000)
myAccount.deposit(1000)
myAccount.withdraw(4000)
print(myAccount.get_Balance())



    