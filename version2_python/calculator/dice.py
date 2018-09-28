import random

class Dice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)

    def __str__(self):
        return "d{}".format(self.faces)
