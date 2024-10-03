import sys
input = sys.stdin.readline

def printboard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="\t")
        print()
    print()

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        if dp[y][x] != 0 and not ((x,y) == (N-1, N-1)):
            if 0 <= y+board[y][x] < N:
                dp[y+board[y][x]][x] += dp[y][x]
            if 0 <= x+board[y][x] < N:
                dp[y][x+board[y][x]] += dp[y][x]
            
            # printboard(dp)

print(dp[-1][-1])
