import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]

for i in range(N):
    sums.append(sums[i] + nums[i])

result = float("-inf")

for i in range(N-K+1):
    # print(result, sums[i+K-1] - sums[i])
    result = max(result, sums[i+K] - sums[i])

# print(sums)
print(result)
