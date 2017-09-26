#battle
from characters.base import Character
# from characters.womping_willow import Womping_willow
from characters.wizard import Wizard
# from characters.voldemort import Voldemort
# from store import *
# from sword import *
# from tonic import *
import time
import random

class Battle(object):
    def do_battle(self, wizard, enemy):
        print("=====================")
        print("{} faces the {}".format(wizard.name, enemy.name))
        print("=====================")
        while wizard.alive() and enemy.alive():
            wizard.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                wizard.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(wizard)
        if wizard.alive():
            print("You defeated the {}".format(enemy.name))
            return True
        else:
            print("You lost the battle!")
            return False
