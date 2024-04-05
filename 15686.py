from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i, j))
        elif board[i][j] == 1:
            houses.append((i, j))


result = float("inf")
combs = list(combinations(chickens, M))
for comb in combs:
    curchkdst = 0
    for house in houses:
        minhouse = float("inf")
        for chk in comb:
            curdist = abs(house[0]-chk[0])+abs(house[1]-chk[1])
            minhouse = min(curdist, minhouse)
        curchkdst += minhouse

    result = min(result, curchkdst)

print(result)
