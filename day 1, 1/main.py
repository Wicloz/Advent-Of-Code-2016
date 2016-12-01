visited = [[0, 0]]
direction = 0

input = "L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4,"
list = input.split(' ')

for move in list:
    if move[:1] is 'L':
        direction -= 1
    if move[:1] is 'R':
        direction += 1
    if direction == 4:
        direction = 0
    if direction == -1:
        direction = 3

    steps = int(move[1:-1])
    for i in range(0, steps):
        if direction == 0:
            visited += [[visited[-1][0] + 1, visited[-1][1]]]
        if direction == 1:
            visited += [[visited[-1][0], visited[-1][1] + 1]]
        if direction == 2:
            visited += [[visited[-1][0] - 1, visited[-1][1]]]
        if direction == 3:
            visited += [[visited[-1][0], visited[-1][1] - 1]]

        for place in visited[:-1]:
            if place[0] == visited[-1][0] and place[1] == visited[-1][1]:
                print(abs(place[0]) + abs(place[1]))

print(abs(visited[-1][0]) + abs(visited[-1][1]))
