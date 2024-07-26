import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
prices.insert(0, 0)

dp = [prices[1]*i for i in range(N+1)]

for card in range(2, N+1):
    for cardcnt in range(card, N+1):
        if dp[cardcnt] > dp[cardcnt-card]+prices[card]:
            dp[cardcnt] = min(dp[cardcnt], dp[cardcnt-card]+prices[card])

print(dp[-1])
