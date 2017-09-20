#medic character

from characters.base import Character
import random

class Medic(Character):
    def __init__ (self, name, health = 15, power = 2):
        super().__init__(name)
        self.health = health
        self.power = power
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)

    def print_status(self):
        super().print_status()

    def heal(self):
        prob = random.randint(1, 5)
        if prob == 1:
            self.health += 2
        else:
            pass
