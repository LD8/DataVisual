from random import randint

class Die:
    '''a model of a die'''

    def __init__(self, sides=6):
        # die sides can be customised
        self.sides = sides

    def roll(self):
        # generate a random number between 1 and die sides
        return randint(1, self.sides)