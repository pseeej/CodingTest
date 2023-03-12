import sys
input = sys.stdin.readline

N, M = map(int, input().split())

book = []

for _ in range(M):
    days, pages = map(int, input().split())
    book.append([days, pages])

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    day = book[i-1][0]
    page = book[i-1][1]
    for j in range(1, N+1):
        if j >= day:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day]+page)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])
