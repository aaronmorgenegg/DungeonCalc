class Encounter:
    def __init__(self, units=[], global_status=[]):
        self.round_count = 0
        self.current_unit = 0
        self.global_status = global_status
        self.units = units



