class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initalAmount,accoName):
        self.balance = initalAmount
        self.name = accoName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, Account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self , amount):
        try: 
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nwithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdraw interrupted: {error}")

    def transfer(self, amount , account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✅\n\n*********')
        except BalanceException as error:
            print(f"Tranfer interrupted.❌" '{error}')