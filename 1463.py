N = int(input())

dp = [0, 0, 1, 1]
for i in range(4, N+1):
    tmp = float("inf")
    if i%3 == 0:
        tmp = min(dp[i//3]+1, dp[i-1]+1)

    if i%2 == 0:
        tmp = min(tmp, (min(dp[i//2]+1, dp[i-1]+1)))
    
    dp.append(min(tmp, dp[i-1]+1))

print(dp[N])
