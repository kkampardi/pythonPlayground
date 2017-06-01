import random

''' abstract coin, general class for all coins '''

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        """ loop over kwargs """
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads


        if self.is_rare:
            self.value = self.original_value * 1.5
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    ''' define the distructor '''
    def __del__(self):
        print("Coin Spend!")

    ''' chance the value of heads var'''
    def flip(self):
        options = [True, False]
        choice = random.choice(options)
        self.heads = choice



""" create Pounds inherriting the Coin general class """


class Pound(Coin):
    ''' store all data about the coin within a dict '''
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenesh",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        ''' lete the parent function do the rest '''
        super().__init__(**data)


class one_pence(Coin):
    """ store all data about the coin within a dict """
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }
        ''' lete the parent function do the rest '''
        super().__init__(**data)

class tow_pence(Coin):
    """ store all data about the coin within a dict """
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        ''' lete the parent function do the rest '''
        super().__init__(**data)


class five_pence(Coin):
    """ store all data about the coin within a dict """
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 22,
            "thickness": 2.85,
            "mass": 7.12
        }
        ''' lete the parent function do the rest '''
        super().__init__(**data)

        """ override rust function,  polymorphism """
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


coins = [one_pence(), tow_pence(), five_pence()]