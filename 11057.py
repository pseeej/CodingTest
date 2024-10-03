import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0] = [1 for _ in range(10)]

for i in range(1, N):
    dp[i][0] = 1
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# print(dp)

print(sum(dp[N-1])%10007)
