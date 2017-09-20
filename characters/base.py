#base character
import random

class Character:
    def __init__ (self, name):
        self.name = name
        # self.health = health
        # self.power = power
        # self.coins = coins

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        if self.health > 0:
            print("{}: {} health and {} power".format(self.name, self.health, self.power))
        elif self.health <= 0:
            print('{} is dead.'.format(self.name))

    def bounty(enemy, x):
        enemy.coins += x
