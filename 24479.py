from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# dfs
def dfs(graph, node, visited, vTF):
    # 들어간 순서를 기억해줘야 함. 이거때문에 헤맸음,.,^^
    global cnt
    # 방문 처리
    vTF[node-1]= 1
    # 방문하지 않은 애일 경우
    if visited[node-1] == 0:
        visited[node-1] = cnt
        cnt += 1

    # 다음 노드로 넘어가기 위한 과정
    for n in graph[node-1]:
        if vTF[n-1] == 0:
            dfs(graph, n, visited, vTF)

n, m, r = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2)
    graph[v2-1].append(v1)

for i in range(n):
    graph[i].sort(reverse=False)


visited = [0 for _ in range(n)]
vTF = [0 for _ in range(n)]
cnt = 1

dfs(graph, r, visited, vTF)
for i in visited[:]:
    print(i)
