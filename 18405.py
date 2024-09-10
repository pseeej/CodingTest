from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

S, Y, X = map(int, input().split())

tovisit = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            tovisit.append([board[i][j], i, j, 1])

tovisit.sort()
tovisit = deque(tovisit)

while tovisit:
    vid, y, x, time = tovisit.popleft()
    # print(vid, y, x, time)

    if time > S:
        break

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dy, dx in d:
        ny, nx = dy+y, dx+x

        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
            tovisit.append([vid, ny, nx, time+1])
            board[ny][nx] = vid

        if ny == Y-1 and nx == X-1:
            print(vid)
            exit() 

    # print(time, board)
    
print(board[Y-1][X-1])
