import sys
from collections import defaultdict
input = sys.stdin.readline

M, N = map(int, input().split())

compares = defaultdict(list)
for m in range(1, M+1):
    nums = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                compares[m].append(">")
            elif nums[i] == nums[j]:
                compares[m].append("=")
            else:
                compares[m].append("<")

cnt = 0
for i in range(1, M):
    for j in range(i+1, M+1):
        if compares[i] == compares[j]:
            cnt += 1

print(cnt)
