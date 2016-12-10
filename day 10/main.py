import robot
import output

def fill_bots(bots, til):
    for i in range(len(bots), til + 1):
        bot = robot.Robot()
        bots.append(bot)

def fill_outputs(outputs, til):
    for i in range(len(outputs), til + 1):
        out = output.Output()
        outputs.append(out)

input = open('input.txt', 'r')
bots = []
outputs = []

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
    else:
        fill_outputs(outputs, bot.high_to_num)
        bot.high_to = outputs[bot.high_to_num]
    if bot.low_to_type == "bot":
        bot.low_to = bots[bot.low_to_num]
    else:
        fill_outputs(outputs, bot.low_to_num)
        bot.low_to = outputs[bot.low_to_num]

for x in range(9999):
    for bot in bots:
        bot.work()

for i in range(len(outputs)):
    print("Output", i, ":")
    for chip in outputs[i].chips:
        print(chip)

print(outputs[0].chips[0] * outputs[1].chips[0] * outputs[2].chips[0])
