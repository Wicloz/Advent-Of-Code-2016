class Robot:
    def __init__(self):
        self.chips = []

    def set_instruction(self, low, high, low_type, high_type):
        self.high_to_num = high
        self.low_to_num = low
        self.high_to_type = high_type
        self.low_to_type = low_type

    def add_chip(self, value):
        if len(self.chips) < 2:
            self.chips.append(value)
        else:
            raise IndexError("Robot can't hold anymore chips");

    def work(self):
        if len(self.chips) == 2:
            if (self.chips[1] < self.chips[0]):
                high, low = self.chips
            else:
                low, high = self.chips
            if self.high_to_type == "bot":
                self.high_to.work()
                self.high_to.add_chip(high)
            if self.low_to_type == "bot":
                self.low_to.work()
                self.low_to.add_chip(low)
            self.chips = []

    def check(self):
        return len(self.chips) == 2 and ((self.chips[0] == 61 and self.chips[1] == 17) or (self.chips[0] == 17 and self.chips[1] == 61))
