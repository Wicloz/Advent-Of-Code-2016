import room

sum_sectors = 0
input = open('input.txt', 'r')

for line in input:
    this_room = room.Room(line)
    if this_room.real():
        sum_sectors += this_room.sid
        this_room.decrypt()
        print(this_room.room_dec, ':', this_room.sid)

print(sum_sectors)
