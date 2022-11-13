import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
colors = []

for _ in range(N):
    colors.append(tuple(map(int, input().split())))

gomduri = tuple(map(int, input().split()))

if N <= 7:
    limit = N
else:
    limit = 7

result = float("inf")
for cnt in range(2, limit+1):
    combs = list(combinations(colors, cnt))
    for comb in combs:
        tmpcalc = 0
        rgb = [0 for _ in range(3)]
        for i in range(cnt):
            for j in range(3):
                rgb[j] += comb[i][j]
        
        for i in range(3):
            tmpcalc += abs(rgb[i]//cnt - gomduri[i])

        if tmpcalc < result:
            result = tmpcalc

print(result)
