lr = 0
ud = 2

keypad = [
    ['x', 'x', '1', 'x', 'x'],
    ['x', '2', '3', '4', 'x'],
    ['5', '6', '7', '8', '9'],
    ['x', 'A', 'B', 'C', 'x'],
    ['x', 'x', 'D', 'x', 'x'],
]

input = open('input.txt', 'r')

for move in input:
    for step in move:
        if step is 'D' and ud < 4:
            if keypad[ud+1][lr] is not 'x':
                ud += 1
        if step is 'U' and ud > 0:
            if keypad[ud-1][lr] is not 'x':
                ud -= 1
        if step is 'R' and lr < 4:
            if keypad[ud][lr+1] is not 'x':
                lr += 1
        if step is 'L' and lr > 0:
            if keypad[ud][lr-1] is not 'x':
                lr -= 1
    print(keypad[ud][lr])

input.close()
