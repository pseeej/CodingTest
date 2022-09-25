from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
fam1, fam2 = map(int, input().split())
M = int(input())

family = defaultdict(list)
to_visit = set(i for i in range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)
# print()
# DFS로 해볼겡
def DFS(cur, cnt):
    for next in family[cur]:
        if next in to_visit:
            to_visit.remove(next)
            #print(next, cnt)
            if next == fam2:
                print(cnt+1)
                exit()
            cnt = DFS(next, cnt+1)

    return cnt-1



to_visit.remove(fam1)
cnt = DFS(fam1, 0)
if fam2 in to_visit:
    print("-1")
