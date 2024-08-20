import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [float("inf") for _ in range(max(N, K)*2+1)]

tovisit = deque()
tovisit.append(N)
dp[N] = 0

while tovisit:
    # 갈 수 있는 곳 : curr-1, curr+1, curr*2
    currp = tovisit.popleft()

    if currp-1 >= 0 and dp[currp-1] > dp[currp]+1:
        dp[currp-1] = dp[currp]+1
        tovisit.append(currp-1)
    if currp+1 < len(dp) and dp[currp+1] > dp[currp]+1:
        dp[currp+1] = dp[currp]+1
        tovisit.append(currp+1)
    if currp*2 < len(dp) and dp[currp*2] > dp[currp]+1:
        dp[currp*2] = dp[currp]+1
        tovisit.append(currp+1)

print(dp[K])
