input = open('input.txt', 'r')
count = 0

for line in input:
    abas = []
    babs = []
    in_brackets = False

    for i in range(0, len(line) - 2):
        if (line[i] is '[' and not in_brackets) or (line[i] is ']' and in_brackets):
            in_brackets = not in_brackets

        if in_brackets:
            if line[i] is not line[i+1] and line[i] is line[i+2]:
                bab = line[i] + line[i+1] + line[i]
                aba = line[i+1] + line[i] + line[i+1]
                babs.append(bab)
                if aba in abas:
                    count += 1
                    break
        else:
            if line[i] is not line[i+1] and line[i] is line[i+2]:
                aba = line[i] + line[i+1] + line[i]
                bab = line[i+1] + line[i] + line[i+1]
                abas.append(aba)
                if bab in babs:
                    count += 1
                    break

print(count)
input.close()
