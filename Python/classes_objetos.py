# How to create a class


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value


account = Account("Jamilton", 1000)
# account.deposit(100)
account.withdraw(100)
print(f'Conta: {account.name}\nSaldo: {account.balance}')


account_maria = Account("Maria", 800)
account_maria.deposit(500)
account_maria.withdraw(100)
print(f'Conta: {account_maria.name}\nSaldo: {account_maria.balance}')
