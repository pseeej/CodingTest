from itertools import combinations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

points = []
for i in range(N):
    for j in range(M):
        points.append((i,j))

combs = list(combinations(points, K))
result = -float("inf")
for comb in combs:
    checkIfDone = False
    
    newcomb = set(comb)
    for point in comb:
        newcomb.remove(point)
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        y, x = point
        for dy, dx in d:
            ny, nx = dy+y, dx+x

            if (ny, nx) in newcomb:
                checkIfDone = True
                break

        if checkIfDone:
            break

    if not checkIfDone:
        tmpsum = 0
        for point in comb:
            py, px = point
            tmpsum += board[py][px]

        result = max(result, tmpsum)

print(result)
        
