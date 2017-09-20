from characters.base import Character
from characters.hero import Hero
from characters.medic import Medic
from characters.shadow import Shadow
import random

def main():
    x = input('Hero name: ')
    hero = Hero(x)
    # x = input('Medic name: ')
    medic = Medic('Medic')
    shadow = Shadow('Shadow')
    hero.print_status()
    shadow.print_status()

    while shadow.alive() and hero.alive():
        # hero.print_status()
        # shadow.print_status()
        print()
        print("What do you want to do?")
        print("1. fight shadow")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(shadow)
            hero.print_status()
            shadow.print_status()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if shadow.alive():
            shadow.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
