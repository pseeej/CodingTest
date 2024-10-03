import sys
input = sys.stdin.readline

N = int(input())
jumps = []

for _ in range(N-1):
    jumps.append(list(map(int, input().split())))

K = int(input())

dp = [[float("inf"), float("inf")] for _ in range(N)]
dp[0] = [0, 0]

for i in range(N-1):
    dp[i+1][0] = min(dp[i+1][0], dp[i][0]+jumps[i][0])
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+jumps[i][0])
    if i+2 < N:
        dp[i+2][0] = min(dp[i+2][0], dp[i][0]+jumps[i][1])
        dp[i+2][1] = min(dp[i+2][1], dp[i][1]+jumps[i][1])
    if i+3 < N:
        dp[i+3][1] = min(dp[i+3][1], dp[i][0]+K)

    # print(i, dp)

print(min(dp[-1]))
