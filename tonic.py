from characters.base import Character
from characters.goblin import Goblin
from characters.hero import Hero
from characters.wizard import Wizard
# from battle import *
# from store import *
# from sword import *
import time
import random

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))
