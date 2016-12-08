class Screen:
    def __init__(self):
        self.pixels = [[False for x in range(50)] for y in range(6)]

    def display(self):
        for i in range(0, 6):
            for j in range(0, 50):
                print('#' if self.pixels[i][j] else ' ', end='')
            print()

    def active_pixels(self):
        count = 0
        for i in range(6):
            for j in range(50):
                if self.pixels[i][j]:
                    count += 1
        return count

    def mod_rect(self, w, h):
        for i in range(h):
            for j in range(w):
                self.pixels[i][j] = True

    def mod_row(self, row, offset):
        copy = self.pixels[row].copy()
        for i in range(50):
            self.pixels[row][i] = copy[(i - offset) % 50]

    def mod_col(self, col, offset):
        copy = [self.pixels[i][col] for i in range(6)]
        for i in range(6):
            self.pixels[i][col] = copy[(i - offset) % 6]
