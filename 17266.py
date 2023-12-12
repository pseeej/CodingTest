import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
points = list(map(int, input().split()))

way = [0 for _ in range(N+1)]
dist = max(points[0], N-points[-1], 0)


for i in range(1, M):
    calc = abs(points[i]-points[i-1])
    if calc%2 == 0:
        dist = max(dist, calc//2)
    else:
        dist = max(dist, calc//2+1)

print(dist)
