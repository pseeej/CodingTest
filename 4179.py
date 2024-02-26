from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))

qjihoon = deque()
qfire = deque()
vjihoon = [[0 for _ in range(C)] for _ in range(R)]
vfire = [[0 for _ in range(C)] for _ in range(R)]


for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            jihoon = (i, j)
            qjihoon.append(jihoon)
            vjihoon[i][j] = 1
        if board[i][j] == 'F':
            fire = (i, j)
            qfire.append(fire)
            vfire[i][j] = 1

def BFS():
    diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while qfire:
        y, x = qfire.popleft()

        for i in range(4):
            dy, dx = diff[i]
            newy, newx = y+dy, x+dx

            if 0 <= newy < R and 0 <= newx < C:
                if not (vfire[newy][newx]) and board[newy][newx] != "#":
                    vfire[newy][newx] = vfire[y][x] + 1
                    qfire.append((newy, newx))

    while qjihoon:
        y, x = qjihoon.popleft()
                    
        for i in range(4):
            dy, dx = diff[i]
            newy, newx = y+dy, x+dx

            if 0 <= newy < R and 0 <= newx < C:
                if board[newy][newx] != '#' and not(vjihoon[newy][newx]):
                    if not vfire[newy][newx] or vfire[newy][newx] > vjihoon[y][x] + 1:
                        vjihoon[newy][newx] = vjihoon[y][x] + 1
                        qjihoon.append((newy, newx))

            else:
                return vjihoon[y][x]


    return "IMPOSSIBLE"

print(BFS())
