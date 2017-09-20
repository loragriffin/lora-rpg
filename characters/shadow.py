#shadow character

from characters.base import Character
import random

class Shadow(Character):
    def __init__ (self, name, health = 10, power = 2):
        super().__init__(name)
        self.health = health
        self.power = power
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)

    def print_status(self):
        super().print_status()

    def block(self, enemy):
        prob = random.randint(1, 5)
        return prob

    def bounty(enemy):
        enemy.coins += 5
