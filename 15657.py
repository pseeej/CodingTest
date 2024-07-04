import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

results = []
def DFS(depth, nums, suyeol):
    if depth >= M:
        results.append(suyeol)
        return

    for num in nums:
        idx = nums.index(num)
        DFS(depth+1, nums[idx:], suyeol+[num])

for num in nums:
    idx = nums.index(num)
    DFS(1, nums[idx:], [num])


for result in results:
    result.sort()
    print(' '.join(map(str, result)))
