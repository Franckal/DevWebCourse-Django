"""
Polymorphism -> Quality or state of being able to assume
                different forms
"""


class Animal:  # Superclass
    def __init__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight

    def run(self):
        print('run like a')

    def sleep(self):
        print('sleep')

    def __str__(self):
        return f'Color: {self.color}, Size: {self.size}, Weight: {self.weight}'


class Dog(Animal):  # Subclass
    def __init__(self, color, size, weight):
        super().__init__(color, size, weight)
        self.weight = f'{weight} Kg'
        #self.breed = breed

    def bark(self):
        print('bark')

    # Override
    def run(self):
        super().run()
        print('dog')

    def __str__(self):
        return super().__str__() + f', Breed: {self.breed}'


class Bird(Animal):  # Subclass
    def __init__(self, color, size, weight):
        super().__init__(color, size, weight)

    def fly(self):
        print('fly')

    # Override
    def run(self):
        super().run()
        print('bird')


class Parrot(Bird, Dog):
    def __init__(self, color, size, weight):
        super().__init__(color, size, weight)

    def run(self):
        print('correr')

    def speak(self):
        print('Speak')


# dog = Dog('Brown', '40cm', '1', 'Golden')
# print(dog)
# dog.run()

parrot = Parrot('Yellow', '30cm', '500g')
parrot.run()  # Animal
parrot.fly()  # Bird
parrot.speak()  # Parrot
parrot.bark()  # Dog

