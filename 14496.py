from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = defaultdict(list)
counts = [float("inf") for _ in range(N+1)]
counts[a] = 0

for _ in range(M):
    v, x = map(int, input().split())
    graph[v].append(x)
    graph[x].append(v)

tovisit = []
heappush(tovisit, (0, a))

while tovisit:
    dist, node = heappop(tovisit)

    if counts[node] < dist:
        continue

    for nextnode in graph[node]:
        if counts[nextnode] > dist + 1:
            counts[nextnode] = dist+1
            heappush(tovisit, (dist+1, nextnode))


if counts[b] == float("inf"):
    print(-1)
else:
    print(counts[b])
