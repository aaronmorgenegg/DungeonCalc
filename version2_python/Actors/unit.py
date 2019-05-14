from version2_python.Config.settings import *
from version2_python.Dice.dice import rollInitiative

class Unit:
    def __init__(self, name, hp=0, armor=0, initiative=0, initiative_mod=0, note="", status=[]):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.initiative = initiative
        self.initiative_mod = initiative_mod
        self.note = note
        self.status = status

    def updateTurn(self):
        self.__updateStatus()

    def updateRound(self):
        self.__updateInitiative()

    def removeStatus(self, status_name):
        self.status = [status for status in self.status if status.name != status_name]

    def __updateInitiative(self):
        if REROLL_INITIATIVE_EACH_ROUND is True:
            self.initiative = rollInitiative(self.initiative_mod)

    def __updateStatus(self):
        for status in self.status:
            status.update()
            if not status.isActive(): print("{} has expired".format(status.name))

        self.status = [x for x in self.status if x.isActive()]

    def printSimple(self):
        string = ""

        name = "Name: {}".format(self.name)
        string += name

        hp = "Health: {}".format(self.hp)
        string += ", {}".format(hp)

        armor = "Armor: {}".format(self.armor)
        string += ", {}".format(armor)

        initiative = "Initiative: {}".format(self.initiative)
        string += ", {}".format(initiative)

        status = "Status: "
        for s in self.status:
            status += str(s) + ", "
        if len(self.status) > 0: string += ", {}".format(status)

        note = "Notes: {}".format(self.note)
        if len(self.note) > 0: string += "{}".format(note)

        return string

    def __str__(self):
        return self.printSimple()
