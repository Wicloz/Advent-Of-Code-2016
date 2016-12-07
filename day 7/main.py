import re

def has_abba(word):
    for i in range(0, len(word) - 3):
        if word[i] is word[i+3] and word[i+1] is word[i+2] and word[i] is not word[i+1]:
            return True
    return False

input = open('input.txt', 'r')
count = 0

for line in input:
    outside = list(filter(None, re.findall(r"(.*?)(?:\[.*?\]|$)", line)))
    inside = re.findall(r"\[(.*?)\]", line)
    if sum([has_abba(w) for w in outside]) > 0 and not sum([has_abba(w) for w in inside]) > 0:
        count += 1

print(count)
input.close()
