# Q1. Create a 
# BankAccount 
# class with attributes account_number, owner_name, 
# and balance. 
# Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Example usage
# Creating a bank account
account = BankAccount("123456789", "John Doe", 1000)
# Checking balance
account.check_balance()
# Depositing money
account.deposit(500)
# Withdrawing money
account.withdraw(200)
# Checking balance again
account.check_balance()            

