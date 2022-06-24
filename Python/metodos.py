# Methods
# Register email:   ja@gmail.com    password:1234


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.addresses = list()

    def __str__(self):
        return f'email: {self.email}, senha: {self.password}'

    def __iter__(self):
        return self.addresses.__iter__()

    def _validate(self):
        register_email = 'ja@gmail.com'
        register_password = '1234'

        if register_email == self.email and register_password == self.password:
            print('Valid User!')
        else:
            print('Invalid User!')

    def login(self):
        self._validate()
        # authenticate
        print('Send data')

    def password_strength(self):
        if len(self.password) >= 5:
            return True
        else:
            return False

    def register_address(self, *addresses):
        for address in addresses:
            print(f"Address: {address}")


user = User('ja@gmail.com', '1234')
user.addresses = ['Street 1', 'Street 2', 'Street 3']

for address in user:
    print(f"Address: {address}")

print(user)
# user.login()
# if user.password_strength():
#     print('Strong password!')
# else:
#     print('Weak password!')

# list_address = ['Street 1', 'Street 2']
# user.register_address(*list_address)
# user.register_address('Street 1', 'Street 2')
# print(user)
