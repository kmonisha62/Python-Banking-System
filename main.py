from abc import ABC, abstractmethod
from datetime import datetime


# ==========================================
# ABSTRACT CLASS
# ==========================================
class BankAccount(ABC):

    def __init__(self, account_number, name, balance=0):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance
        self.__transactions = []

    # Get account number
    def get_account_number(self):
        return self.__account_number

    # Get account holder name
    def get_name(self):
        return self.__name

    # Get balance
    def get_balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

            transaction = (
                f"Deposited ₹{amount} "
                f"on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
            )

            self.__transactions.append(transaction)

            print("\nAmount deposited successfully!")
            print("Current Balance: ₹", self.__balance)

        else:
            print("\nPlease enter a valid amount.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("\nPlease enter a valid amount.")

        elif amount > self.__balance:
            print("\nInsufficient balance!")

        else:
            self.__balance -= amount

            transaction = (
                f"Withdrawn ₹{amount} "
                f"on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
            )

            self.__transactions.append(transaction)

            print("\nAmount withdrawn successfully!")
            print("Current Balance: ₹", self.__balance)

    # Show transaction history
    def show_transactions(self):

        print("\n========== TRANSACTION HISTORY ==========")

        if len(self.__transactions) == 0:
            print("No transactions available.")

        else:
            for transaction in self.__transactions:
                print(transaction)

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass


# ==========================================
# SAVINGS ACCOUNT
# ==========================================
class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"


# ==========================================
# CURRENT ACCOUNT
# ==========================================
class CurrentAccount(BankAccount):

    def account_type(self):
        return "Current Account"


# ==========================================
# BANKING SYSTEM
# ==========================================
class BankingSystem:

    def __init__(self):
        self.accounts = {}

    # Create account
    def create_account(self):

        print("\n========== CREATE ACCOUNT ==========")

        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            print("Account already exists!")
            return

        name = input("Enter account holder name: ")

        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter your choice: ")

        if choice == "1":

            account = SavingsAccount(
                account_number,
                name
            )

        elif choice == "2":

            account = CurrentAccount(
                account_number,
                name
            )

        else:
            print("Invalid choice!")
            return

        self.accounts[account_number] = account

        print("\nAccount created successfully!")
        print("Account Number:", account_number)
        print("Account Holder:", name)
        print("Account Type:", account.account_type())

    # Find account
    def find_account(self):

        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            return self.accounts[account_number]

        print("\nAccount not found!")
        return None

    # Deposit money
    def deposit_money(self):

        print("\n========== DEPOSIT MONEY ==========")

        account = self.find_account()

        if account:

            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number.")

    # Withdraw money
    def withdraw_money(self):

        print("\n========== WITHDRAW MONEY ==========")

        account = self.find_account()

        if account:

            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number.")

    # Check balance
    def check_balance(self):

        print("\n========== CHECK BALANCE ==========")

        account = self.find_account()

        if account:

            print("Account Holder:", account.get_name())
            print("Account Type:", account.account_type())
            print("Current Balance: ₹", account.get_balance())

    # Transaction history
    def transaction_history(self):

        print("\n========== TRANSACTION HISTORY ==========")

        account = self.find_account()

        if account:
            account.show_transactions()

    # Account details
    def account_details(self):

        print("\n========== ACCOUNT DETAILS ==========")

        account = self.find_account()

        if account:

            print("Account Number:", account.get_account_number())
            print("Account Holder:", account.get_name())
            print("Account Type:", account.account_type())
            print("Balance: ₹", account.get_balance())


# ==========================================
# MAIN PROGRAM
# ==========================================

bank = BankingSystem()

while True:

    print("\n")
    print("======================================")
    print("       PYTHON BANKING SYSTEM")
    print("======================================")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Account Details")
    print("7. Exit")

    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        bank.create_account()

    elif choice == "2":

        bank.deposit_money()

    elif choice == "3":

        bank.withdraw_money()

    elif choice == "4":

        bank.check_balance()

    elif choice == "5":

        bank.transaction_history()

    elif choice == "6":

        bank.account_details()

    elif choice == "7":

        print("\nThank you for using Python Banking System!")
        print("Have a nice day!")
        break

    else:

        print("\nInvalid choice! Please try again.")