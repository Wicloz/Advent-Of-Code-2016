office = []
positions_current = [(1, 1)]
positions_next = []
positions_visited = [(1, 1)]
steps = 0
done = False

while not done:
    for pos in positions_current:
        if pos == (31, 39):
            done = True
            break

        for t in [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]:
            if t[0] < 0 or t[1] < 0 or t in positions_visited:
                continue

            while len(office) <= t[0]:
                office.append([])
            for i in range(len(office[t[0]]), t[1] + 1):
                num = t[0]*t[0] + 3*t[0] + 2*t[0]*i + i + i*i + 1362
                open = bin(num).count('1') % 2 == 0
                office[t[0]].append(open)

            if office[t[0]][t[1]] or t == (31, 39):
                positions_next.append(t)
                positions_visited.append(t)

    positions_current = positions_next
    positions_next = []
    steps += 1

print(steps - 1)
