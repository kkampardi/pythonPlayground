import random


class Wizard:
    def __init__(self, name, level ):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks to hero {}".format(self.name, creature.name))

        my_roll = random.randint(1, 12)
        creature_roll = random.randint(1, 12)

        print("You roll {} ...".format(my_roll))
        print("{} rolls {}".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has beeing DEFEATED!!!")
            return False


class Creature:
    """
        level, name
    """

    # initializer for creature obj
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
