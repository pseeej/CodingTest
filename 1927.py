import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    ord = int(input())
    if ord == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr))

    else:
        heappush(arr, ord)

