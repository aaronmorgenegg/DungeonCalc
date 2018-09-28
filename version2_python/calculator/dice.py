import random


class Dice:
    def __init__(self, faces=6):
        self.faces = faces

    def roll(self, n=1):
        """
        Roll dice n number of times, default 1

        :param n: Number of times to roll
        :return: result of dice roll
        """
        result = random.randint(1, self.faces)
        if n <= 1: return result
        return self.roll(n-1) + result

    def __str__(self):
        return "d{}".format(self.faces)
