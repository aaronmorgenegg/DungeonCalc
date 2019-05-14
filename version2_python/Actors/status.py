
class Status:
    def __init__(self, name, time_total, note=None):
        self.name = name
        self.time_total = time_total
        self.time_remaining = time_total
        self.note = note

    def update(self):
        self.time_remaining -= 1

    def isActive(self):
        if self.time_remaining <= 0: return False
        return True

    def printSimple(self):
        name = self.name
        time = "Time: {}/{}".format(self.time_remaining, self.time_total)
        note = "Notes: {}".format(self.note)
        return "{}({}, {})".format(name, time, note)

    def __str__(self):
        return self.printSimple()
