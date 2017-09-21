from characters.base import Character
from characters.goblin import Goblin
from characters.hero import Hero
from characters.wizard import Wizard
from battle import Battle
from store import Store
from sword import Sword
from tonic import Tonic

import time
import random

if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("YOU WIN!")
