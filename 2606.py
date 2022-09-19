from collections import defaultdict

N = int(input())
M = int(input())

graph = defaultdict(list)
to_visit = set()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    to_visit.add(a)
    to_visit.add(b)


# DFS 쓸래
def DFS(to_visit, cur, cnt):
    for num in graph[cur]:
        if num in to_visit:
            to_visit.remove(num)
            cnt = DFS(to_visit, num, cnt+1)

    return cnt


to_visit.remove(1)
print(DFS(to_visit, 1, 0))
            
