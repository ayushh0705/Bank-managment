# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class bank():

    def __init__(self):
        
        self.account = {}

    def create_account(self, account_number, initial_balance=0):

        if account_number not in self.account:
            self.account[account_number] = initial_balance
            print(f"The account is created successfully for the {account_number}")
        else:
            print(f"The account {account_number} has already exist")

    def display_balance(self, account_number):
        if account_number in self.account:
            balance = self.account[account_number]
            print(f"the balance of the {account_number} is ${balance}")

        else:
            print(f"the {account_number} does not exist")

    def deposite(self, account_number, amount):
        if account_number in self.account:
            self.account[account_number] += amount
            print(f"The added amount is successfully deposited into your account {amount}")
        else:
            print(f"The acount {account_number} does not exist")
            self.display_balance = account_number

    def withdraw(self, account_number, withdraw, amount):

        if account_number in self.account:
            if self.account[account_number] >= amount:
                self.account[account_number] -= withdraw
                print(f"The amount {amount:.2f} has been successfully withdraw from your account")
                self.display_balance[account_number]
            else:
                print(f"{account_number} has insufficient balance")
        else:
            print(f"the account {account_number} does not exist")



bank = bank()
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.deposite(acno1, wamt1)

    