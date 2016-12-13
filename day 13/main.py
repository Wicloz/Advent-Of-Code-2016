office = []
positions_current = [(1, 1)]
positions_next = []
positions_visited = [(1, 1)]

for step in range(50):
    for pos in positions_current:
        for t in [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]:
            if t[0] < 0 or t[1] < 0 or t in positions_visited:
                continue

            while len(office) <= t[0]:
                office.append([])
            for i in range(len(office[t[0]]), t[1] + 1):
                num = t[0]*t[0] + 3*t[0] + 2*t[0]*i + i + i*i + 1362
                open = bin(num).count('1') % 2 == 0
                office[t[0]].append(open)

            if office[t[0]][t[1]]:
                positions_next.append(t)
                positions_visited.append(t)

    positions_current = positions_next
    positions_next = []

print(len(positions_visited))
