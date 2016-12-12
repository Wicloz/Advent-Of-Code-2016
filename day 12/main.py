input = open('input.txt', 'r')
lines = input.readlines()
input.close()

regs = {'a':0, 'b':0, 'c':0, 'd':0}
index = 0

while index < len(lines):
    instruction = lines[index].split()
    if instruction[0] == 'cpy':
        if instruction[1].isnumeric():
            regs[instruction[2]] = int(instruction[1])
        else:
            regs[instruction[2]] = regs[instruction[1]]
    elif instruction[0] == 'inc':
        regs[instruction[1]] += 1
    elif instruction[0] == 'dec':
        regs[instruction[1]] -= 1
    if instruction[0] == 'jnz' and ((instruction[1].isnumeric() and int(instruction[1]) != 0) or (regs[instruction[1]] != 0)):
        index += int(instruction[2])
    else:
        index += 1

print(regs['a'])
