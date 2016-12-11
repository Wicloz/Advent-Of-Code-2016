import copy

class Facility:
    chips = [['Pr'], [], ['Co', 'Cu', 'Ru', 'Pl'], []]
    generators = [['Pr'], ['Co', 'Cu', 'Ru', 'Pl'], [], []]
    current_floor = 0
    last_move = []

    def copy(self):
        other = Facility()
        other.chips = copy.deepcopy(self.chips)
        other.generators = copy.deepcopy(self.generators)
        other.current_floor = self.current_floor
        other.last_move = copy.deepcopy(self.last_move)
        return other

    def valid(self):
        for i in range(4):
            if len(self.generators[i]) > 0:
                for chip in self.chips[i]:
                    if chip not in self.generators[i]:
                        return False
        return True

    def done(self):
        for i in range(3):
            if len(self.chips[i]) > 0 or len(self.generators[i]) > 0:
                return False
        return True

    def perform_move(self, to_floor, chips, generators):
        self.last_move = [self.current_floor, chips, generators]
        for chip in chips:
            self.chips[self.current_floor].remove(chip)
        self.chips[to_floor] += chips
        for gen in generators:
            self.generators[self.current_floor].remove(gen)
        self.generators[to_floor] += generators
        self.current_floor = to_floor

    def find_moves(self):
        moves = []

        chips = self.chips[self.current_floor]
        for i in range(len(chips)):
            if self.current_floor < 3:
                moves.append([self.current_floor + 1, [chips[i]], []])
            if self.current_floor > 0:
                moves.append([self.current_floor - 1, [chips[i]], []])
            for j in range(i + 1, len(chips)):
                if self.current_floor < 3:
                    moves.append([self.current_floor + 1, [chips[i], chips[j]], []])
                if self.current_floor > 0:
                    moves.append([self.current_floor - 1, [chips[i], chips[j]], []])

        generators = self.generators[self.current_floor]
        for i in range(len(generators)):
            if self.current_floor < 3:
                moves.append([self.current_floor + 1, [], [generators[i]]])
            if self.current_floor > 0:
                moves.append([self.current_floor - 1, [], [generators[i]]])
            for j in range(i + 1, len(generators)):
                if self.current_floor < 3:
                    moves.append([self.current_floor + 1, [], [generators[i], generators[j]]])
                if self.current_floor > 0:
                    moves.append([self.current_floor - 1, [], [generators[i], generators[j]]])

        for chip in chips:
            for generator in generators:
                if self.current_floor < 3:
                    moves.append([self.current_floor + 1, [chip], [generator]])
                if self.current_floor > 0:
                    moves.append([self.current_floor - 1, [chip], [generator]])

        if self.last_move in moves:
            moves.remove(self.last_move)
        return moves

    def get_next_states(self):
        states = []
        for move in self.find_moves():
            other = self.copy()
            other.perform_move(*move)
            if other.valid():
                states.append(other)
        return states
