from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 얘는 이전 거와 다르게 연결이 안 되어있는 애들도 다 방문을 해봐야함
tovisit = set(i for i in range(1, N+1))
graph = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

nums = list(tovisit)
cnt = 0

# 이번엔 BFS로 해볼게용.
nextnum = deque()

cur = nums[0]
for num in nums:
    if num not in tovisit:
        continue
    
    cur = num
    nextnum.append(cur)
    while nextnum:
        cur = nextnum.popleft()
        for next in graph[cur]:
            if next in tovisit:
                nextnum.append(next)
                tovisit.remove(next)

    cnt += 1

print(cnt)
