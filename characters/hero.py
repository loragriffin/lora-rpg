#hero character

from characters.base import Character
import random

class Hero(Character):
    def __init__ (self, name, health = 20, power = 4, coins = 5):
        super().__init__(name)
        self.health = health
        self.power = power
        self.coins = coins
        super().alive()

    def print_status(self):
        super().print_status()

    def attack(self, enemy):
        prob = random.randint(1, 10)
        if prob == 1:
            enemy.health -= (self.power * 2)
            print('You did {} damage.'.format(self.power * 2))
        else:
            enemy.health -= self.power
            print('You did {} damage.'.format(self.power))
