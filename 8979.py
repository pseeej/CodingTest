import sys
input = sys.stdin.readline

N, K = map(int, input().split())
find = []
medals = list()

for i in range(N):
    tmp = list(map(int, input().split()))
    if tmp[0] == K:
        find = tmp[1:]
    medals.append(tmp[1:])

medals.sort(reverse=True)

for i in range(N):
    if medals[i] == find:
        print(i+1)
        break
