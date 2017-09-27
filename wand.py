from characters.base import Character
# from characters.womping_willow import Womping_willow
# from characters.voldemort import Voldemort
from characters.wizard import Wizard
# from battle import *
# from store import *
# from tonic import *
import time
import random

class Wand(object):
    cost = 10
    name = 'wand'
    power = 'Gives you +2 power!'

    def apply(self, wizard):
        wizard.power += 2
        print("{}'s power increased to {}.".format(wizard.name, wizard.power))
