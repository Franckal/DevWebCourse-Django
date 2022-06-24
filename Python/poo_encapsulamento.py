"""
Pillar 2 - Encapsulation
"""


class Filter:
    def __init__(self, image):
        self.image = image

    def black_and_white(self):
        print(f'{self.image} with black and white filter.')

    def aged_photo(self):
        print(f'{self.image} with aged filter.')


# filter_test = Filter('franck_photo')
# filter_test.black_and_white()

# #### Access control and Getters & Setters #### #


class Account:
    def __init__(self, balance):
        self._number = 0
        self._balance = balance

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value > 0:
            self._number = value
        else:
            print('Invalid Number!')

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value


account = Account(800)
account.number = 0
print(account.number)
account.withdraw(100)
account.deposit(200)



