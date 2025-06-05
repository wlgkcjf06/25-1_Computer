class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Please enter a positive amount!")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Please enter a positive amount!")
        elif amount > self.__balance:
            raise Exception("The withdraw amount must not exceed balance!")
        else:
            self.__balance-=amount

    def getBalance(self):
        return self.__balance

    def __repr__(self):
        return f"Bank Account, Owner = {self.owner}, Balance = {self.__balance}"