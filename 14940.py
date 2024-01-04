import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
nextvisit = []
for i in range(N):
    board.append(list(map(int, input().split())))
    if 2 in board[i]:
        heappush(nextvisit, [0, i, board[i].index(2)])

answer = [[float("inf") for _ in range(M)] for _ in range(N)]
visited = set()
while nextvisit:
    now = heappop(nextvisit)
    dist, y, x = now[0], now[1], now[2]

    if (y, x) in visited:
        continue

    visited.add((y, x))
    answer[y][x] = dist

    if y+1<N and board[y+1][x] != 0 and answer[y+1][x] > dist+1:
        heappush(nextvisit, [dist+1, y+1, x])
    if x+1<M and board[y][x+1] != 0 and answer[y][x+1] > dist+1:
        heappush(nextvisit, [dist+1, y, x+1])
    if y-1>=0 and board[y-1][x] != 0 and answer[y-1][x] > dist+1:
        heappush(nextvisit, [dist+1, y-1, x])
    if x-1>=0 and board[y][x-1] != 0 and answer[y][x-1] > dist+1:
        heappush(nextvisit, [dist+1, y, x-1])


for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(0, end=" ")
        elif answer[i][j] == float("inf"):
            print(-1, end=" ")
        else:
            print(answer[i][j], end=" ")
    print()
        
        

