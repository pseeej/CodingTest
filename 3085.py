import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input().strip()))


def countColor(pan, N):
    maxcnt = 0
    for i in range(N):
        garo = 1
        sero = 1
        for j in range(1, N):
            if j-1 >= 0 and board[i][j] == board[i][j-1]:
                garo += 1
            elif j-1 >= 0 and board[i][j] != board[i][j-1]:
                maxcnt = max(garo, maxcnt)
                garo = 1

            if j-1 >= 0 and board[j][i] == board[j-1][i]:
                sero += 1
            elif j-1 >= 0 and board[j][i] != board[j-1][i]:
                maxcnt = max(sero, maxcnt)
                sero = 1

        maxcnt = max(maxcnt, garo, sero)

    return maxcnt

result = 0

for i in range(N):
    for j in range(N):
        if j+1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            result = max(result, countColor(board, N))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if j+1 < N and board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            result = max(result, countColor(board, N))
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]


print(result)
