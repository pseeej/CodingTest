import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
prices.insert(0, 0)

dp = [0 for _ in range(N+1)]

for totcnt in range(1, N+1):
    for card in range(1, totcnt+1):
        dp[totcnt] = max(dp[totcnt], dp[totcnt-card]+prices[card])

print(dp[-1])
