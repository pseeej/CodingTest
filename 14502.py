from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [] 
for _ in range(N):
    board.append(list(map(int, input().split())))

zeros = []
viruses = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zeros.append((i, j))
        elif board[i][j] == 2:
            viruses.append((i, j))

def DFS(y, x):
    global board
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] in {2, 0}:
            board[ny][nx] = -1
            DFS(ny, nx)
        
    return board

def printboard():
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end="\t")
        print()
    print()

combs = list(combinations(zeros, 3))
realboard = deepcopy(board)
result = 0

for comb in combs:
    board = deepcopy(realboard)

    for point in comb:
        y, x = point
        board[y][x] = 1


    for virus in viruses:
        vy, vx = virus
        if board[vy][vx] == 2:
            board[vy][vx] = -1
            DFS(vy, vx)
        
    tmp = 0
    for i in range(N):
        tmp += board[i].count(0)
    
    if result < tmp:
        result = tmp
        # print(comb, result)
        # printboard()

print(result)
        
