from copy import deepcopy
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
numsums = deepcopy(nums)

for i in range(1, N):
    numsums[i] = numsums[i-1]+nums[i]

if numsums[-1] < S:
    print("0")
    exit()

for i in range(N):
    if nums[i] >= S:
        print(1)
        exit()

start = 0
end = 0
for i in range(N):
    if numsums[i] >= S:
        end = i
        break

result = end-start+1

while start <= end <= N-1:
    if numsums[end]-numsums[start] < S:
        end += 1
    else:
        result = min(result, end-start)
        start += 1

print(result)
