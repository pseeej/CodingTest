from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    graph[g].sort()

visited = set()

sequence = [0 for _ in range(N+1)]

sequence[R] = 1
visited.add(R)

trial = 2

def DFS(now):
    global trial
    if len(visited) == N:
        return
    
    for g in graph[now]:
        if g not in visited:
            sequence[g] = trial
            visited.add(g)
            trial += 1

            DFS(g)

    return

DFS(R)

for i in range(1, N+1):
    print(sequence[i])
