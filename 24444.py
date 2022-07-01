import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2)
    graph[v2-1].append(v1)

for i in range(n):
    graph[i].sort()

visited = [0 for _ in range(n)]
queue = deque()
queue.append(r)

cnt = 1
visited[r-1] = cnt

while queue:
    node = queue.popleft()
    for item in graph[node-1]:
        if visited[item-1] == 0:
            cnt += 1
            visited[item-1] = cnt
            queue.append(item)

for i in range(n):
    print(visited[i])
