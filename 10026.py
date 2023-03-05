import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

board = []
for _ in range(N):
    usript = input().rstrip()
    tmp = []
    for u in usript:
        tmp.append(u)
    board.append(tmp)

board2 = deepcopy(board)

# 안 적록색약
def DFS_np(board, i, j, N, color):
    board[i][j] = '.'

    if i > 0 and board[i-1][j] == color:
        DFS_np(board, i-1, j, N, color)
    if j > 0 and board[i][j-1] == color:
        DFS_np(board, i, j-1, N, color)
    if i < N-1 and board[i+1][j] == color:
        DFS_np(board, i+1, j, N, color)
    if j < N-1 and board[i][j+1] == color:
        DFS_np(board, i, j+1, N, color)


cnt_np = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != '.':
            cnt_np += 1
            DFS_np(board, i, j, N, board[i][j])


# 적록색약
def DFS_rg(board, i, j, N, color):
    board[i][j] = '.'

    if i > 0 and board[i-1][j] == color:
        DFS_rg(board, i-1, j, N, color)
    if j > 0 and board[i][j-1] == color:
        DFS_rg(board, i, j-1, N, color)
    if i < N-1 and board[i+1][j] == color:
        DFS_rg(board, i+1, j, N, color)
    if j < N-1 and board[i][j+1] == color:
        DFS_rg(board, i, j+1, N, color)

for i in range(N):
    for j in range(N):
        if board2[i][j] == 'R':
            board2[i][j] = 'G'


cnt_rg = 0
for i in range(N):
    for j in range(N):
        if board2[i][j] != '.':
            cnt_rg += 1
            DFS_rg(board2, i, j, N, board2[i][j])


print(cnt_np, cnt_rg)
