"""
Association relationship -> Is one of the most common
    relationships between two objects, it happens when
    an object "Uses" another, however, without them
    depending on each other
"""

# teste = ''
# teste3 = None  # Null
# del teste3

# if teste3 == teste:
#     print('True')
# else:
#     print('False')

# print('teste')


class Person:
    def __init__(self, name):
        self.name = name
        self.video_game = None

    def walk(self):
        print(f'Person ({self.name}) walking')


class VideoGame:
    def __init__(self, name):
        self.name = name

    def running_game(self):
        print(f'Running game in {self.name}')


person = Person('Franck')
videogame = VideoGame('Xbox')

person.video_game = videogame
person.video_game.running_game()
