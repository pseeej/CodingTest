import sys
input = sys.stdin.readline

T = int(input())
dp = [0, 1, 2, 4]
for _ in range(T):
    num = int(input())
    for i in range(len(dp), num+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])

    print(dp[num])

