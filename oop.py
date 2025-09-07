from bank_account import *

dave = BankAccount(1000, "dave")
sara = BankAccount(2000, "sara")

dave.getBalance()
sara.getBalance()

sara.deposit(500)

dave.withdraw(100)

dave.transfer(100,sara)

sara.getBalance()
sara.transfer(200,dave)

dave.getBalance()
sara.getBalance()
dave.withdraw(100)
dave.transfer(200,sara)
dave.getBalance()
sara.withdraw(1000)

dave.transfer(1000,sara)