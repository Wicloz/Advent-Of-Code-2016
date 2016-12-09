input = open('input.txt', 'r')

compressed = input.read()
decompressed = ''
input.close()

amount = 0
repeats = 0
rep_string = ''

skip = 0
for i in range(len(compressed)):
    if i < skip:
        continue

    if amount > 0:
        rep_string += compressed[i]
        amount -= 1
    if amount == 0 and repeats > 0:
        while repeats > 0:
            decompressed += rep_string
            repeats -= 1
        continue

    if amount == 0:
        if compressed[i] is '(':
            amount, repeats = [int(x) for x in compressed[i+1:compressed.find(')', i)].split('x')]
            skip = compressed.find(')', i) + 1
            rep_string = ''

        elif compressed[i] is not '\n':
            decompressed += compressed[i]

print(decompressed)
print(len(decompressed))
