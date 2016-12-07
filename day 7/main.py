input = open('input.txt', 'r')
count = 0

for line in input:
    abas = []
    in_brackets = False
    for i in range(0, len(line) - 2):
        if (line[i] is '[' and not in_brackets) or (line[i] is ']' and in_brackets):
            in_brackets = not in_brackets

print(count)
input.close()
