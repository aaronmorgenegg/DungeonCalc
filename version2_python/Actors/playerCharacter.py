from version2_python.Actors.unit import Unit


class PlayerCharacter(Unit):
    def __init__(self, name, nicknames, hp, armor, initiative, initiative_mod, note, player):
        super().__init__(name, nicknames, hp, armor, initiative, initiative_mod, note)
        self.player = player

    def printSimple(self):
        player = "Player: {}".format(self.player)
        return "{},{}".format(player, super().printSimple())

    def printDetail(self):
        # TODO:
        return self.printSimple()

    def __str__(self):
        return self.printSimple()
