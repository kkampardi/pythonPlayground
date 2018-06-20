import random

import time

from pygames.wizard_game.actors import Creature, Wizard


def main():
    header()
    game_loop()


def header():
    print('-------------------------')
    print('     Wizard Game App')
    print('-------------------------')


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    print(creatures)

    hero = Wizard('Gandolf', 75)
    while True:
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest ...'
              .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizarnd runs and takes time to recover ... ")
                time.sleep(5)
                print("The wizard returns revitalized")
        if cmd == 'r':
            print('run')
        elif cmd == 'l':
            print('The Wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of leve {}'.format(c.name, c.level))

if __name__ == '__main__':
    main()