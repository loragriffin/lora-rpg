from characters.base import Character
from characters.goblin import Goblin
from characters.hero import Hero
from characters.wizard import Wizard
from battle import *
from sword import *
from tonic import *
import time
import random

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            answer = int(input("> "))
            if answer == 10:
                break
            else:
                ItemToBuy = Store.items[answer - 1]
                item = ItemToBuy()
                hero.buy(item)
