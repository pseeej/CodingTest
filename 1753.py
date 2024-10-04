from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

costs = [float("inf") for _ in range(V+1)]
costs[K] = 0

tovisit = []
heappush(tovisit, (costs[K], K))

while tovisit:
    currcost, currnode = heappop(tovisit)

    if costs[currnode] < currcost:
        continue

    for next in graph[currnode]:
        nextnode, nextcost = next
        if costs[nextnode] > currcost + nextcost:
            heappush(tovisit, (nextcost+currcost, nextnode))
            costs[nextnode] = currcost + nextcost


for i in range(1, V+1):
    if costs[i] == float("inf"):
        print("INF")
    else:
        print(costs[i])
