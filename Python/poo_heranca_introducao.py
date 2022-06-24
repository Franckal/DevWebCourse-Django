# Inheritance - Reuse and maintenance
# Class: Dog | Bird


class Animal:
    def __init__(self):
        self.color = ''
        self.size = ''
        self.weight = ''

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):
    def bark(self):
        print('bark')


class Bird(Animal):
    def fly(self):
        print('fly')


dog = Dog()
# dog.color = 'Brown'
# dog.run()
# print(dog.color)

bird = Bird()
bird.color = 'Yellow'
bird.run()
bird.fly()
