from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

tovisit = []
dists = [float("inf") for _ in range(N+1)]
# 거리, 좌표
heappush(tovisit, [0, 1])

while tovisit:
    tmp = heappop(tovisit)
    cost, curnode = tmp[0], tmp[1]

    if dists[curnode] < cost:
        continue

    for next in graph[curnode]:
        nextcost, nextnode = next[1], next[0]
        if nextcost + cost < dists[nextnode]:
            dists[nextnode] = nextcost+cost
            heappush(tovisit, [nextcost+cost, nextnode])


print(dists[N])
            
