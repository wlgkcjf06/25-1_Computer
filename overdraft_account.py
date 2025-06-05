from account import BankAccount

class OverdraftAccount(BankAccount):
    def __init__(self, owner, initial_balance = 0, overdraft_limit = 100):
        super().__init__(owner, initial_balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Please enter a positive amount!")
        elif (self._BankAccount__balance - amount) < -self.__overdraft_limit:
            raise Exception("The balance after withdraw is lower than the overdraft limit!")
        else:
            self._BankAccount__balance -= amount

    def __repr__(self):
        return f"Overdraft Account, Owner = {self.owner}, Balance = {self._BankAccount__balance}, Overdraft Limit = {self.__overdraft_limit}"