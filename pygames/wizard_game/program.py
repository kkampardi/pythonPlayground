from pygames.wizard_game.actors import Creature, Wizard


def main():
    header()

    game_loop()


def header():
    print('-------------------------')
    print('     Wizard Game App')
    print('-------------------------')


def game_loop():
    creatures = {
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    }

    print(creatures)

    hero = Wizard('Gandolf', 75)
    while True:
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')

        if cmd == 'a':
            print('attack')
        if cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')



if __name__ == '__main__':
    main()