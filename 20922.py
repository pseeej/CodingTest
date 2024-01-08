from collections import defaultdict
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0

answer = 0
numcnts = defaultdict(int)
while True:
    if right == N:
        break
    
    if numcnts[nums[right]] < K:
        numcnts[nums[right]] += 1
        right += 1
    else:
        numcnts[nums[left]] -= 1
        left += 1

    if answer < right-left:
        answer = right-left

print(answer)

