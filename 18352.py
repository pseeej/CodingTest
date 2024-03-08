from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dists = [float("inf") for _ in range(N+1)]
dists[X] = 0

tovisit = deque()
for node in graph[X]:
    tovisit.append([node, 1])

while tovisit:
    now = tovisit.popleft()
    curnode, curdist = now[0], now[1]

    if curdist >= dists[curnode]:
        continue

    dists[curnode] = curdist

    for node in graph[curnode]:
        tovisit.append([node, curdist+1])

# print(dists)

count = []
for i in range(N+1):
    if dists[i] == K:
        count.append(i)

if len(count) == 0:
    print(-1)
else:
    count.sort()
    for c in count:
        print(c)
