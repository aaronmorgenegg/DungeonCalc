from version2_python.Config.settings import *
from version2_python.FileManager.dummyFileManager import DummyFileManager
from version2_python.FileManager.pickleFileManager import PickleFileManager


class Encounter:
    def __init__(self, units=[], global_status=[]):
        self.round_count = 0
        self.current_unit = 0
        self.global_status = global_status
        self.units = units
        self._initFileManager()

    def _initFileManager(self):
        if FILE_MANAGER == 'pickle':
            self.file_manager = PickleFileManager()
        else:
            print("WARNING: Using dummy file manager")
            self.file_manager = DummyFileManager()

    def lookupName(self, name):
        for unit in self.units:
            if name == unit.name or name in unit.nicknames:
                return unit
        for status in self.status:
            if name == status.name or name in status.nicknames:
                return status
        raise Exception("Error: lookupName failed for name {}".format(name))

    def addUnit(self, unit):
        # TODO: make unit names unique
        self.units.append(unit)

    def deleteUnit(self, name):
        unit = self.lookupName(name)
        self.units.remove(unit)

    def update(self):
        self._updateUnits()
        self._updateStatus()
        self._updateRound()

    def _updateRound(self):
        self.round_count += 1
        self.current_unit = 0
        self.sortUnits()

    def _updateUnits(self):
        for unit in self.units:
            unit.updateRound()

    def _updateStatus(self):
        for status in self.global_status:
            status.update()

    def nextTurn(self):
        self.units[self.current_unit].updateTurn()
        self.current_unit += 1
        if self.current_unit >= len(self.units):
            self.current_unit = 0
            self.update()

    def sortUnits(self):
        self.units.sort(key=lambda x: x.initiative, reverse=True)

    def __str__(self):
        header = "-----ENCOUNTER-----"
        round = "Round : {}".format(self.round_count+1)

        status = ""
        if len(self.global_status) > 0: status = "Global Status Effects"
            for i in range(len(self.global_status)):
                status_string = self.global_status[i].printSimple()
                status = "  {}\n    {}".format(status, status_string)

        units = "Units: \n"
        for i in range(len(self.units)):
            unit_string = self.units[i].printSimple()
            if self.current_unit == i:
                units += "  {}\n ** {}".format(units, unit_string)
            else:
                units += "  {}\n    {}".format(units, unit_string)

        return "{}\n{}\n{]\n{}\n".format(header, round, status, units)

