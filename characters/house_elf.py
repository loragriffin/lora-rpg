#medic/house elf character

from characters.base import Character
import random

class House_Elf(Character):
    def __init__ (self, name, health = 15, power = 2, coins = 0):
        super().__init__()
        # self.health = health
        # self.power = power
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)

    def print_status(self):
        super().print_status()

    def heal(self):
        prob = random.randint(1, 5)
        if prob == 1:
            self.health += 2
            print('You gained 2 health.')
        else:
            print('You did not gain health.')
