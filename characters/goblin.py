#goblin character
from characters.base import Character
# from characters.hero import Hero
# from characters.wizard import Wizard
# from battle import *
# from store import *
# from sword import *
# from tonic import *
# import time
# import random

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
