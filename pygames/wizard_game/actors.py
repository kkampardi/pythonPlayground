class Wizard:
    def __init__(self, name, level ):
        self.name = name
        self.level = level

     #def attack(self, other_creature):




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
