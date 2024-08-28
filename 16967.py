import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
board = []
for _ in range(H+X):
    board.append(list(map(int, input().split())))

orgboard = [[0 for _ in range(W)] for _ in range(H)]

def printBoard(arr, N, M):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end=" ")
        print()

for i in range(H):
    for j in range(W):
        if i < X:
            orgboard[i][j] = board[i][j]
        elif j < Y:
            orgboard[i][j] = board[i][j]
        elif j >= Y:
            orgboard[i][j] = board[i][j] - orgboard[i-X][j-Y]

printBoard(orgboard, H, W)


