from version2_python.Actors.actor import Actor


class Status(Actor):
    def __init__(self, names, time_total, hp_delta=0, armor_delta=0, initiative_delta=0,
                 hp_mod=0, armor_mod=0, initiative_mod=0, note=None):
        self.names = names
        self.time_total = time_total
        self.time_remaining = time_total
        self.hp_delta = hp_delta
        self.armor_delta = armor_delta
        self.initiative_delta = initiative_delta
        self.hp_mod = hp_mod
        self.armor_mod = armor_mod
        self.initiative_mod = initiative_mod
        self.note = note

    def update(self):
        self.time_remaining -= 1

    def printSimple(self):
        name = "Name: {}".format(self.names)
        time = "Time: {}/{}".format(self.time_remaining, self.time_total)
        note = "Notes: {}".format(self.note)
        return "{},{},{}".format(name, time, note)


    def printDetail(self):
        # TODO:
        return self.printSimple()

    def __str__(self):
        return self.printSimple()
