class Encounter:
    def __init__(self, units=[], global_status=[]):
        self.round_count = 0
        self.current_unit = 0
        self.global_status = global_status
        self.units = units

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
            unit.update()

    def _updateStatus(self):
        for status in self.global_status:
            status.update()

    def nextTurn(self):
        self.current_unit += 1
        if self.current_unit >= len(self.units):
            self.current_unit = 0
            self.update()

    def sortUnits(self):
        self.units.sort(key=lambda x: x.initiative, reverse=True)

    def __str__(self):
        # TODO
        return ""

