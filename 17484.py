import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


costs = [[(float("inf"), 0) for _ in range(M)] for _ in range(N)]
for i in range(M):
    costs[0][i] = (board[0][i], 0)

# way => 왼쪽아래, 바로아래, 오른쪽아래

results = []
def DFS(nboard, cboard, y, x, result):
    if y == N-1:
        result.append(cboard[y][x])
        return
    
    curr = cboard[y][x][0]
    way = cboard[y][x][1]
    if way != 1 and y+1 < N and x-1 >= 0:
        cboard[y+1][x-1] = (curr+nboard[y+1][x-1], 1)
        DFS(nboard, cboard, y+1, x-1, result)
    if way != 2 and y+1 < N:
        cboard[y+1][x] = (curr+nboard[y+1][x], 2)
        DFS(nboard, cboard, y+1, x, result)
    if way != 3 and y+1 < N and x+1 < M:
        cboard[y+1][x+1] = (curr+nboard[y+1][x+1], 3)
        DFS(nboard, cboard, y+1, x+1, result)


for i in range(M):
    DFS(board, costs, 0, i, results)


print(min(results)[0])
    
    
