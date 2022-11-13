import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1 for _ in range(N)]

maxnum = dp[0]

for i in range(N):
    num = nums[i]
    for j in range(i):
        if num < nums[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))

