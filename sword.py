from characters.base import Character
from characters.goblin import Goblin
from characters.hero import Hero
from characters.wizard import Wizard
from battle import *
from store import *
from tonic import *
import time
import random

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))
