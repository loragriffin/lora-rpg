#wizard/witch hero character

from characters.base import Character
import time
import random

class Wizard(Character):
    def __init__(self, name, health = 10, power = 5, coins = 20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def restore(self):
        self.health = 10
        print("Your heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)
