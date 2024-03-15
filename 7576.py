from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

resultboard = [[float("inf") for _ in range(M)] for _ in range(N)]

nextnode = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            nextnode.append((i, j, 0))

diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while nextnode:
    # print(nextnode)
    y, x, currday = nextnode.popleft()

    if currday > resultboard[y][x]:
        continue

    resultboard[y][x] = currday

    for dy, dx in diff:
        # print(y+dy, x+dx)
        if 0 <= y+dy < N and 0 <= x+dx < M and board[y+dy][x+dx] == 0 and resultboard[y+dy][x+dx] > currday+1:
            resultboard[y+dy][x+dx] = currday+1
            nextnode.append((y+dy, x+dx, currday+1))

maxday = -1
for i in range(N):
    for j in range(M):
        # print(resultboard[i][j], end=" ")
        if board[i][j] == -1:
            continue
        else:
            maxday = max(maxday, resultboard[i][j])
    # print()

if maxday == float("inf"):
    print(-1)
else:
    print(maxday)
