import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [float("inf") for _ in range(K+1)]
dp[0] = 0

for i in range(K+1):
    for coin in coins:
        if i+coin <= K:
            dp[i+coin] = min(dp[i+coin], dp[i]+1)

# print(dp)
if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])
