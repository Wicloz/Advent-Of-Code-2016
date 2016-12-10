import robot

def fill_bots(bots, til):
    for i in range(len(bots), til + 1):
        bot = robot.Robot()
        bots.append(bot)

input = open('input.txt', 'r')
bots = []

for line in input:
    words = line.split()
    if words[0] == 'value':
        botnum = int(words[5])
        fill_bots(bots, botnum)
        bots[botnum].add_chip(int(words[1]))
    else:
        botnum = int(words[1])
        fill_bots(bots, botnum)
        bots[botnum].set_instruction(int(words[6]), int(words[11]), words[5], words[10])

input.close()

for bot in bots:
    if bot.high_to_type == "bot":
        bot.high_to = bots[bot.high_to_num]
    if bot.low_to_type == "bot":
        bot.low_to = bots[bot.low_to_num]

answer = -1
while answer < 0:
    for i in range(len(bots)):
        if bots[i].check():
            answer = i
            break
        bots[i].work()

print(answer)
