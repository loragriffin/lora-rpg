from characters.base import Character
# from characters.womping_willow import Womping_willow
# from characters.voldemort import Voldemort
# from characters.wizard import Wizard
# from battle import *
# from store import *
# from sword import *
import time
import random

class Elixir(object):
    cost = 5
    name = 'elixir'
    power = 'Gives you +2 health!'
    
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))
