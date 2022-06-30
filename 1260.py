from collections import defaultdict
from collections import deque

# dfs
def dfs(graph, start, visited):
    # 방문 체크
    visited[start-1] = 1
    print(start, end= " ")
    # 현재 위치하고 있는 node에서 이어질 수 있는 모든 다른 노드들 중
    # 방문하지 않은 노드들에 한해서만 재귀로 반복
    for node in graph[start-1]:
        if visited[node-1] == 0:
            dfs(graph, node, visited)

# bfs
def bfs(graph, start, visited):
    # 덱에 넣어주고 방문 체크
    queue = deque([start])
    visited[start-1] = 1
    # 덱에 원소가 남아있지 않을 때까지 진행
    while queue:
        # 시작은 덱에서 제일 왼쪽에 있는 걸로.
        v = queue.popleft()
        print(v, end=" ")
        # 현재 노드에서 뻗어나갈 수 있는 애들 중에서
        # 방문하지 않은 노드를 기준으로 감
        # 너비탐색이기 때문에 순서대로 그냥 덱의 오른쪽에 들어감
        for i in graph[v-1]:
            if visited[i-1] == 0:
                visited[i-1] = 1
                queue.append(i)

n, m, v = map(int, input().split())

# 특정 노드에 대해 뻗어나갈 수 있는 모든 길들을 list로 저장해둠
graph = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2)
    graph[v2-1].append(v1)

for i in range(n):
    graph[i].sort()

visit = [0 for _ in range(n)]
dfs(graph, v, visit)
print()

# 방문 노드 갱신해줘야함
# python의 list는 call by reference라 이렇게 안 해주면
# bfs에서는 위에서 사용한 visit 리스트를 그대로 다시 사용하게 됨
visit = [0 for _ in range(n)]
bfs(graph, v, visit)
