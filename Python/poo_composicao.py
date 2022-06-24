"""
Relação de Composição -> a classe principal (todo) cria
    uma instância da outra classe (parte), que se torna parte
    Quando a classe principal for destrida, sua instancia da
    outra classe também será
"""


class User:  # all
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def __del__(self):
        print(f'{self.name} APAGADO')

    def insert_address(self, cep, city, street):
        address = Address(cep, city, street)
        self.addresses.append(address)

    def list_addresses(self):
        print(f'{self.name} Addresses')
        for address in self.addresses:
            print(address)


class Address:  # part
    def __init__(self, cep, city, street):
        self.cep = cep
        self.city = city
        self.street = street

    def __del__(self):
        print(f'{self.street} APAGADO')

    def __str__(self):
        return f'CEP: {self.cep}, City: {self.city}, Street: {self.street}'


user = User('Franck')
user.insert_address('123', 'São Paulo', 'Rua Quem, 123')
user.insert_address('321', 'Minas Gerais', 'Rua Qual, 321')

user.list_addresses()
