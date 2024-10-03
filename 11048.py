from copy import deepcopy
import sys
input = sys.stdin.readline

def printboard(board, R, C):
    for i in range(R):
        for j in range(C):
            print(board[i][j], end="\t")
        print()
    print()

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = []
for i in range(N):
    dp.append(deepcopy(board[i]))


d = [(-1, 0), (0, -1), (-1, -1)]

for y in range(N):
    for x in range(M):
        maxdp = 0
        for dy, dx in d:
            ny, nx = y+dy, x+dx

            if 0 <= ny < N and 0 <= nx < M:
                maxdp = max(maxdp, board[y][x]+dp[ny][nx])
        
        if not(y==0 and x==0):
            dp[y][x] = maxdp
        
        # printboard(dp, N, M)

print(dp[-1][-1])

