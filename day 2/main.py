lr = 1
ud = 1

input = open('input.txt', 'r')

for move in input:
    for step in move:
        if step is 'D' and ud < 2:
            ud += 1
        if step is 'U' and ud > 0:
            ud -= 1
        if step is 'R' and lr < 2:
            lr += 1
        if step is 'L' and lr > 0:
            lr -= 1
    print(ud * 3 + lr + 1)
