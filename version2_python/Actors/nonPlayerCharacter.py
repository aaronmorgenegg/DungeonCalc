from version2_python.Actors.unit import Unit


class NonPlayerCharacter(Unit):
    def __init__(self, names, hp, armor, initiative, initiative_mod, note, ai_level, attacks):
        super().__init__(names, hp, armor, initiative, initiative_mod, note)
        self.ai_level = ai_level
        self.attacks = attacks

    def printDetail(self):
        # TODO:
        return self.printSimple()
