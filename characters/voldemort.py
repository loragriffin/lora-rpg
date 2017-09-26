#wizard character
from characters.base import Character
# from characters.goblin import Goblin
# from characters.hero import Hero
# from battle import *
# from store import *
# from sword import *
# from tonic import *
import time
import random

class Voldemort(Character):
    def __init__(self):
        self.name = 'Lord Voldemort'
        self.health = 20
        self.power = 3

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack!".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Voldemort, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power
