from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)

# print(tree)

# 트리에서 해당 값이 몇차에 위치하고 있는지 알기 위해 만듦
global tree_cnt
tree_cnt = dict()
for i in range(1, N+1):
    tree_cnt[i] = 1

to_visit = set(i for i in range(2, N+1))

def DFS(cur, to_visit, tree_cnt):
    cnt = 0

    for next in tree[cur]:
        if next in to_visit:
            cnt += 1
            # 방문처리
            to_visit.remove(next)
            # 차수 처리.
            now_cnt = tree_cnt[cur] + 1
            tree_cnt[next] = now_cnt

            DFS(next, to_visit, tree_cnt)
            
    # 더이상 방문할 애들이 없으면 리턴
    if cnt == 0:
        return

DFS(1, to_visit, tree_cnt)


for i in range(2, N+1):
    smallest = N+1
    parent = 0
    
    # i번째에서 방문할 수 있는 모든 노드들 중
    # 가장 차수가 낮은 거 ==> 부모 라고 생각해서
    # 가장 차수가 낮은 다음 노드?를 찾으려고 했음
    for next in tree[i]:
        if tree_cnt[next] < smallest:            
            smallest = tree_cnt[next]
            parent = next

    print(parent)
