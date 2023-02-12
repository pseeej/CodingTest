import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sums = []
sums.append(nums[0])

for i in range(1, N):
    sums.append(max(nums[i], sums[i-1]+nums[i]))

print(max(sums))
