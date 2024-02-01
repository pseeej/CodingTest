from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

tovisit = []
heappush(tovisit, [0, start])

dists = [float("inf") for _ in range(N+1)]
dists[start] = 0

while tovisit:
    tmp = heappop(tovisit)
    cost, currnode = tmp[0], tmp[1]

    if dists[currnode] < cost:
        continue

    for nextitem in graph[currnode]:
        nextnode, nextcost = nextitem[0], nextitem[1]

        if nextcost+dists[currnode] < dists[nextnode]:
            dists[nextnode] = nextcost+cost
            heappush(tovisit, [nextcost+cost, nextnode])

# print(dists)
print(dists[end])
