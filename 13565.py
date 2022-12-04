import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())

board = []
for _ in range(M):
    tmp = input()
    tmplist = []
    for c in tmp:
        tmplist.append(c)
    board.append(tmplist)

# for i in range(M):
#     for j in range(N):
#         print(board[i][j], end=" ")
#     print()
# print()

def DFS(board, i, j, M, N):
    if board[i][j] == "0":
        board[i][j] = "2"

        if i > 0:
            board = DFS(board, i-1, j, M, N)
        if j > 0:
            board = DFS(board, i, j-1, M, N)
        if i < M-1:
            board = DFS(board, i+1, j, M, N)
        if j < N-1:
            board = DFS(board, i, j+1, M, N)

    return board

for i in range(N):
    if board[0][i] == "0":
        board = DFS(board, 0, i, M, N)

# for i in range(M):
#     for j in range(N):
#         print(board[i][j], end=" ")
#     print()

if "2" in board[-1]:
    print("YES")
else:
    print("NO")
