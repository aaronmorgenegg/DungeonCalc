from version2_python.Config.settings import *
from version2_python.Dice.dice import Dice, rollInitiative

class Unit:
    def __init__(self, name, nicknames=[], hp=0, armor=0, initiative=0, initiative_mod=0, note=None):
        self.name = name
        self.nicknames = nicknames
        self.hp = hp
        self.armor = armor
        self.initiative = initiative
        self.initiative_mod = initiative_mod
        self.note = note
        self.status = []

    def updateTurn(self):
        self.__updateStatus()

    def updateRound(self):
        self.__updateInitiative()

    def __updateInitiative(self):
        if REROLL_INITIATIVE_EACH_ROUND is True:
            self.initiative = rollInitiative(self.initiative_mod)

    def __updateStatus(self):
        for status in self.status:
            status.update()

        self.status = [x for x in self.status if x.isActive() == 0]

    def printSimple(self):
        name = "Name: {}".format(self.name)
        hp = "Health: {}".format(self.hp)
        armor = "Armor: {}".format(self.armor)
        initiative = "Initiative: {}".format(self.initiative)
        status = "Status: {}".format(self.status)
        note = "Notes: {}".format(self.note)
        return "{},{},{},{},{},{}".format(name, hp, armor, initiative, status, note)

    def printDetail(self):
        # TODO:
        return self.printSimple()

    def __str__(self):
        return self.printSimple()
