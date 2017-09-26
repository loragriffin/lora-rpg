#zombie character

from characters.base import Character
import random

class Vampire(Character):
    def __init__ (self, name, health = 20, power = 1):
        super().__init__(name)
        self.health = health
        self.power = power
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)

    def print_status(self):
        print('Vampires cannot die! They are undead.')

    def bounty(enemy):
        enemy.coins += 1

    def undead(self):
        if self.health <= 0:
            self.health += 20
