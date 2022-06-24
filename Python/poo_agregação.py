"""
Aggregation Ratio -> one class needs the other
    to perform its action, is that, one class
    uses the other as part of itself
"""


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if len(self.products) == 0:
            print('ShoppingCart doesnt have products.')
        for product in self.products:
            print(f'{product.name} R$ {product.price}')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def register_product(self):
        pass

    def remove_product(self):
        pass


shoppingcart = ShoppingCart()
product1 = Product('Notebook Acer', 3000)
product2 = Product('Iphone', 8000)
shoppingcart.add_product(product1)
shoppingcart.add_product(product2)

shoppingcart.list_products()