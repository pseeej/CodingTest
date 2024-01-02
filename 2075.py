import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

heap = []
for i in range(N):
    heappush(heap, (-nums[-1][i], N-1, i))
    nums[-1][i] = None

cnt = 0
while cnt < N-1:
    elem = heappop(heap)
    y, x = elem[1], elem[2]
    if y-1 >= 0:
        heappush(heap, (-nums[y-1][x], y-1, x))
        nums[y-1][x] = None

    cnt += 1
    # print(heap)

print(-heappop(heap)[0])
