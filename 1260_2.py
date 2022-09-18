from collections import defaultdict, deque

N, M, V = map(int, input().split())

graph = defaultdict(list)
tovisit = set()

# graph에 양방향으로 집어넣음
# tovisit에 접근할 수 있는 점들을 집어넣음
for _ in range(M):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
    tovisit.add(p1)
    tovisit.add(p2)

# graph에 들어 있는 값 정렬. 작은 값부터 접근할 것이기 때문
for num in tovisit:
    graph[num].sort()


# DFS 함수
def DFS(graph, visit, current):
    print(current, end=" ")

    # 현재 current에서 접근할 수 있는 점들 num으로 하나씩 들어감
    for num in graph[current]:
        # 아직 방문하지 않았을 경우 방문처리 해주고
        # 그 아래의 노드로 또 들어가기
        if num in visit:
            visit.remove(num)
            DFS(graph, visit, num)


# DFS
cur = V
# 방문처리 위한 리스트 카피해서 가져옴
# 카피 안 하면 파이썬 리스트는 call by reference라 전체 내용이 바뀜
visit1 = tovisit.copy()
if cur in visit1:
    visit1.remove(cur)
    DFS(graph, visit1, cur)
else:
    print(cur, end=" ")


print()

# BFS
cur = V
visit2 = tovisit.copy()
nextroute = deque()
print(cur, end=" ")

while True:
    # visit에 존재할 경우 현재 노드 제거
    if cur in visit2:
        visit2.remove(cur)
    # 현재 노드에서 접근할 수 있는 노드들(방문하지 않은 노드들)을 모두
    # nextroute라는 deque에 저장해둠
    # 그리고 방문처리 ㅇㅇ
    for num in graph[cur]:
        if num in visit2:
            print(num, end=" ")
            visit2.remove(num)
            nextroute.append(num)

    # 더이상 방문할 수 있는 노드가 없을 경우 종료
    if not nextroute:
        break
    # 그 다음에 진행될 노드는 방문할 노드들 중 제일 앞의 값
    cur = nextroute.popleft()

