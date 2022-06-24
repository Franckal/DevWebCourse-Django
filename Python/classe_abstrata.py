from abc import ABC, abstractmethod

class Animal(ABC):
    def run(self):
        print('run')

    @abstractmethod
    def breath(self):
        pass


class Dog(Animal):
    def breath(self):
        print('Breath like a dog')


class Bird(Animal):
    def breath(self):
        print('Breath like a bird')


# animal = Animal()
# animal = Animal()
# animal.run()
# dog = Dog()
# dog.run()
# dog.breath()

"""
Bank Account
Account, Checking account and Savings account
"""


class Account(ABC):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, value):
        if value > 0:
            self._balance += value

    def withdraw(self, value):
        if value > 0:
            self._balance -= value


class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, value):
        limit = 300
        if value <= limit:
            self._balance -= value
        else:
            print('Limit exceeded (300)')


class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, value):
        limit = 600
        if value <= limit:
            self._balance -= value
        else:
            print('Limit exceeded (600)')


savings_account = SavingsAccount(10548, 1000)
savings_account.withdraw(500)
print(savings_account.balance)
