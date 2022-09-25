from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

friends = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0 for i in range(N+1)]

# BFS
next_visit = deque()
next_visit.append(1)
depth = 0
visited[1] = 0

while next_visit:
    cur = next_visit.popleft()

    for next in friends[cur]:
        if visited[next] == 0 or visited[cur]+1 < visited[next]:
            visited[next] = visited[cur]+1
            next_visit.append(next)
        

print(visited[2:].count(1) + visited[2:].count(2))
