input = open('input.txt', 'r')
motif = []

for line in input:
    for i in range(0, len(line) - 1):
        if i >= len(motif):
            motif.append({})
        if line[i] not in motif[i]:
            motif[i][line[i]] = 0
        motif[i][line[i]] += 1

word = ''
for i in range(0, len(motif)):
    motif[i] = sorted(motif[i], key=motif[i].__getitem__, reverse=True)
    word += motif[i][0]

print(word)
