from characters.base import Character
from characters.womping_willow import Womping_willow
from characters.wizard import Wizard
from characters.voldemort import Voldemort
from battle import Battle
from store import Store
from wand import Wand
from elixir import Elixir

import time
import random

if __name__ == "__main__":
    # user_input = input('Your wizard\'s name: ')
    wizard = Wizard('Harry')
    enemies = [Womping_willow(), Voldemort()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        wizard_won = battle_engine.do_battle(wizard, enemy)
        if not wizard_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(wizard)

    print("YOU WIN!")
