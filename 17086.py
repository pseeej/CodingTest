from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
sharks = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            sharks.append((i, j))
        else:
            tmp[j] = 9999
    board.append(tmp)

for i in range(N):
    for j in range(M):
        for shark in sharks:
            sharky, sharkx = shark
            dist = max(abs(i-sharky), abs(j-sharkx))
            board[i][j] = min(board[i][j], dist)

# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end=" ")
#     print()

result = 0
for i in range(N):
    result = max(result, max(board[i]))

print(result)
