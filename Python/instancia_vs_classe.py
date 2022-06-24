# Class attribute
# Instance attribute


class Person:
    planet = 'Earth'

    def __init__(self, name):
        self.name = name
        # self.planet = 'Mart'

    def show_name(self):
        print(f'Name: {self.name}')

    @classmethod
    def show_planet(cls):
        print(f'Planet: {cls.planet}')

    @staticmethod
    def recover_habitable_planets():
        print('Earth & Mart')


# print(Person.planet)
# Person.show_planet()
Person.recover_habitable_planets()
franck = Person('Franck')
# franck.name = 'Franck'
# Person.planet = 'Mart'
# print(franck.planet)
franck.show_name()

nayara = Person('Nayara')
# nayara.name = 'Nayara'
# print(nayara.planet)
nayara.show_name()
