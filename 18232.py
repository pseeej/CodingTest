from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
S, E = map(int, input().split())

ways = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    ways[x].append(y)
    ways[y].append(x)

for i in range(1, N+1):
    if i > 1:
        ways[i].append(i-1)
    if i < N:
        ways[i].append(i+1)

# print(ways)

short = dict()
for i in range(1, N+1):
    short[i] = 3000000
short[S] = 0

visited = set()
visited.add(S)

nexts = deque()
nexts.append(S)

# BFS
while nexts:
    cur = nexts.popleft()
    if cur == E:
        break

    for node in ways[cur]:
        if node not in visited:
            visited.add(node)
            if short[node] > short[cur] + 1:
                short[node] = short[cur] + 1
            nexts.append(node)

print(short[E])
