count = 0
input = open('input.txt', 'r')

sets = [[], [], []]

for line in input:
    sides = line[:-1].split()
    sets[0] += [int(sides[0])]
    sets[1] += [int(sides[1])]
    sets[2] += [int(sides[2])]

    if len(sets[0]) == 3:
        for i in range(0, 3):
            possible = True
            if sets[i][0] >= sets[i][1] + sets[i][2]:
                possible = False
            if sets[i][1] >= sets[i][0] + sets[i][2]:
                possible = False
            if sets[i][2] >= sets[i][0] + sets[i][1]:
                possible = False
            if possible:
                count += 1

        sets = [[], [], []]

print(count)

input.close()
