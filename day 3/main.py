count = 0
input = open('input.txt', 'r')

for line in input:
    sides = line[:-1].split()
    possible = True
    if int(sides[0]) >= int(sides[1]) + int(sides[2]):
        possible = False
    if int(sides[1]) >= int(sides[0]) + int(sides[2]):
        possible = False
    if int(sides[2]) >= int(sides[0]) + int(sides[1]):
        possible = False
    if possible:
        count += 1

print(count)

input.close()
