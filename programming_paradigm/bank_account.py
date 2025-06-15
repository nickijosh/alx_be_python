# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add the specified amount to the account balance
        self.account_balance += amount

    def withdraw(self, amount):
        # Withdraw if sufficient balance is available
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Print the current balance
        print(f"Current Balance: ${self.account_balance}")