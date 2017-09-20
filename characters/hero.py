#hero character

from character.base import Character

class Hero:
    def __init__ (self, name, health = 20, power = 4):
        super().__init__(name)
        super().__init__(health)
        super().__init__(power)
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)
