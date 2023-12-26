import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    level, nick = map(str, input().split())
    level = int(level)

    checkIfDone = False
    for i in range(len(rooms)):
        room = rooms[i]
        if len(room[1]) < m and room[0]-10 <= level <= room[0]+10:
            rooms[i][1].append((level, nick))
            checkIfDone = True
            break

    if not checkIfDone:
        rooms.append([level, [(level, nick)]])

# print(rooms)
for i in range(len(rooms)):
    rooms[i][1] = sorted(rooms[i][1], key=lambda k:k[1])
    if len(rooms[i][1]) == m:
        print("Started!")
    else:
        print("Waiting!")

    for j in range(len(rooms[i][1])):
        print(rooms[i][1][j][0], rooms[i][1][j][1])
        
            

