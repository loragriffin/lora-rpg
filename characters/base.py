#base character
import random

class Character:
    def __init__ (self, name):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
