import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

board = []
for _ in range(N):
    usript = input()
    tmp = []
    for u in usript:
        tmp.append(u)
    board.append(tmp)

user = (0, 0)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            user = (i, j)
            break
    if user != (0, 0):
        break

cnt = 0
def DFS(i, j):
    global cnt
    if board[i][j] == 'P':
        cnt += 1
    
    board[i][j] = 'X'

    if i > 0 and board[i-1][j] != 'X':
        DFS(i-1, j)
    if j > 0 and board[i][j-1] != 'X':
        DFS(i, j-1)
    if i < N-1 and board[i+1][j] != 'X':
        DFS(i+1, j)
    if j < M-1 and board[i][j+1] != 'X':
        DFS(i, j+1)

DFS(user[0], user[1])
if cnt==0:
    print('TT')
else:
    print(cnt)
