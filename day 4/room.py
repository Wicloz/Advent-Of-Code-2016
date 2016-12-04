class Room:
    def __init__(self, line):
        self.room_enc, rest = line.rsplit('-', 1)
        self.sid = int(rest.split('[')[0])
        self.checksum = rest.split('[')[1].split(']')[0]

    def real(self):
        letters = {}
        for c in self.room_enc:
            if c is not '-':
                if c not in letters:
                    letters[c] = 1
                else:
                    letters[c] += 1

        letters = sorted(letters.items(), key=self.number_tuple, reverse=True)
        for i in range(0, 5):
            if letters[i][0] not in self.checksum:
                return False
        return True

    def number_tuple(self, tup):
        return tup[1] * 100 - ord(tup[0]) + 96
