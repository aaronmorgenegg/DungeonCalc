from version2_python.Actors.actor import Actor
from version2_python.Config.settings import *
from version2_python.Dice.dice import Dice, rollInitiative

class Unit(Actor):
    def __init__(self, name, nicknames, hp, armor, initiative, initiative_mod, note):
        self.name = name
        self.nicknames = nicknames
        self.hp = hp
        self.armor = armor
        self.initiative = initiative
        self.initiative_mod = initiative_mod
        self.note = note
        self.status = []

    def update(self):
        self.__updateInitiative()
        self.__updateStatus()

    def __updateInitiative(self):
        if REROLL_INITIATIVE_EACH_ROUND is True:
            self.initiative = rollInitiative(self.initiative_mod)

    def __updateStatus(self):
        for status in self.status:
            status.update()
            self.hp += status.hp_delta
            self.armor += status.armor_delta
            self.initiative += status.initiative_delta

        self.status = [x for x in self.status if not x.time_left == 0]

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