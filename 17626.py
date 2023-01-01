N = int(input())

dp = [0, 1]

for i in range(2, N+1):
    tmp = float("inf")
    for j in range(1, int(i**(1/2))+1):
        tmp = min(tmp, dp[i-j**2])
    dp.append(tmp+1)

print(dp[N])
