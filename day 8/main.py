import screen

tinyscreen = screen.Screen()
input = open('input.txt', 'r')

for line in input:
    words = line[:-1].split(' ')
    if words[0] == 'rect':
        tinyscreen.mod_rect(int(words[1].split('x')[0]), int(words[1].split('x')[1]))
    elif words[1] == 'row':
        tinyscreen.mod_row(int(words[2][2:]), int(words[4]))
    elif words[1] == 'column':
        tinyscreen.mod_col(int(words[2][2:]), int(words[4]))

tinyscreen.display()
print(tinyscreen.active_pixels())

input.close()
