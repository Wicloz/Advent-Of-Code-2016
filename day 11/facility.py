import copy

visited = []

class Facility:
    # pairs = [(1, 0), (2, 0)]
    pairs = [(0, 0), (1, 2), (1, 2), (1, 2), (1, 2)]
    current_floor = 0

    def copy(self):
        other = Facility()
        other.pairs = copy.deepcopy(self.pairs)
        other.current_floor = self.current_floor
        return other

    def valid(self):
        dangerfloors = []
        for pair in self.pairs:
            dangerfloors.append(pair[0])
        for pair in self.pairs:
            if pair[0] != pair[1] and pair[1] in dangerfloors:
                return False
        return True

    def done(self):
        for pair in self.pairs:
            if pair[0] != 3 or pair[1] != 3:
                return False
        return True

    def perform_move(self, diff, move1, move2):
        if move1[1] == 0:
            self.pairs[move1[0]] = (self.pairs[move1[0]][0] + diff, self.pairs[move1[0]][1])
        else:
            self.pairs[move1[0]] = (self.pairs[move1[0]][0], self.pairs[move1[0]][1] + diff)
        if move2 != None:
            if move2[1] == 0:
                self.pairs[move2[0]] = (self.pairs[move2[0]][0] + diff, self.pairs[move2[0]][1])
            else:
                self.pairs[move2[0]] = (self.pairs[move2[0]][0], self.pairs[move2[0]][1] + diff)
        self.pairs.sort()
        self.current_floor += diff

    def find_moves(self):
        moves = []
        items = []
        diffs = []

        if self.current_floor > 0:
            diffs.append(-1)
        if self.current_floor < 3:
            diffs.append(1)

        for i in range(len(self.pairs)):
            for j in range(2):
                if self.pairs[i][j] == self.current_floor:
                    items.append((i, j))

        for diff in diffs:
            for i in range(len(items)):
                moves.append([diff, items[i], None])
                for j in range(i + 1, len(items)):
                    moves.append([diff, items[i], items[j]])

        return moves

    def get_next_states(self):
        states = []
        for move in self.find_moves():
            other = self.copy()
            other.perform_move(*move)
            if (other.current_floor, other.pairs) not in visited and other.valid():
                states.append(other)
                visited.append((other.current_floor, other.pairs))
        return states
