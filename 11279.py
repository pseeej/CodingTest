from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    order = int(input())
    if order == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -order)
