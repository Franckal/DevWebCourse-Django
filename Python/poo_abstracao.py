"""
Pillar1 - Abstraction (Part sales and Uber)
Model, Entity, Identity
Characteristics and actions
"""


class Car:
    def __init__(self, model, color, plate):
        self.model = model
        self.color = color
        self.plate = plate

    def display_current_location(self):
        print('Car is in the 10th street')


car = Car("gol", "silver", "JHM-6854")
# car_jamilton = Car("golf", "black", "RTN-2345")


# Virtual store
class Product:
    # Clothes
    # def __init__(self, size, color, price):
    #    self.size = size
    #    self.color = color
    #    self.price = price

    # Electronics
    def __init__(self, width, height, color, price):
        self.width = width
        self.height = height
        self.color = color
        self.price = price


# product = Product("S", "Black", 25.60)
product = Product(70, 60, "black", 25.60)
