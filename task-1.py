class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount} successfully. Current balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Current balance: {self.balance}")
# Example usage:
account1 = BankAccount("John Doe", "1234567890")
account1.deposit(1000)
account1.withdraw(500)
account1.display_balance()