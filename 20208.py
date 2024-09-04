import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M, H = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

milkpoints = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            milkpoints.append((i, j))
        if board[i][j] == 1:
            home = (i, j)

answer = 0
def DFS(y, x, visited, currhealth, cnts):
    global H, answer, milkpoints

    if currhealth - (abs(y-home[0])+abs(x-home[1])) >= 0:
        # print(visited, currhealth)
        answer = max(answer,cnts)
        if answer == len(milkpoints):
            return

    for point in milkpoints:
        py, px = point
        if (py, px) in set(visited):
            continue
        elif currhealth-(abs(py-y)+abs(px-x)) < 0:
            continue
        else:
            visited.append(point)
            DFS(py, px, visited, currhealth-(abs(py-y)+abs(px-x))+H, cnts+1)
            visited.pop()

DFS(home[0], home[1], [home], M, 0)
print(answer)
