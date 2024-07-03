import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

yeols = []

def DFS(depth, nums, yeol):
    if depth == M:
        yeol.sort()
        yeols.append(yeol)
        return
    
    for num in nums:
        idx = nums.index(num)
        DFS(depth+1, nums[idx+1:], yeol+[num])


for num in nums:
    idx = nums.index(num)
    DFS(1, nums[idx+1:], [num])

yeols.sort()
for yeol in yeols:
    print(' '.join(map(str, yeol)))
