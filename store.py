from characters.base import Character
from characters.womping_willow import Womping_willow
from characters.voldemort import Voldemort
from characters.wizard import Wizard
from battle import *
from wand import *
from elixir import *
import time
import random

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Elixir, Wand]
    def do_shopping(self, wizard):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(wizard.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} (${}), {}".format(i + 1, item.name, item.cost, item.power))
            print("3. leave")
            answer = int(input("(1-3) > "))
            if answer == 3:
                break
            elif wizard.coins > 0:
                ItemToBuy = Store.items[answer - 1]
                item = ItemToBuy()
                wizard.buy(item)
            elif wizard.coins <= 0:
                print('You don\'t have enough coins to purchase anything.')
                leave = input('Would you like to leave the store? (y/n) > ').lower()
                if leave == 'y':
                    break
