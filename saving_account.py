from account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, owner, initial_balance=0, min_balance=100):
        super().__init__(owner, initial_balance)
        self.__min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Please enter a positive amount!")
        elif self._BankAccount__balance - amount < self.__min_balance:
            raise Exception("The balance after withdrawal is lower than minimum balance!")
        else:
            self._BankAccount__balance-=amount

    def __repr__(self):
        return f"Saving Account, Owner = {self.owner}, Balance = {self._BankAccount__balance}, Minimum Balance = {self.__min_balance}"
