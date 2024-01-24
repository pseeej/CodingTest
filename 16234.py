import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N, L, R = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
visited = set()
unified = set()
total = 0
ucnt = 0

def DFS(y, x):
    global board, visited, L, R, N, total, ucnt
    visited.add((y, x))
    unified.add((y, x))
    ucnt += 1
    total += board[y][x]

    if y > 0 and (y-1, x) not in visited and L <= abs(board[y][x]-board[y-1][x]) <= R:
        DFS(y-1, x)
    if x > 0 and (y, x-1) not in visited and L <= abs(board[y][x]-board[y][x-1]) <= R:
        DFS(y, x-1)
    if y+1 < N and (y+1, x) not in visited and L <= abs(board[y][x]-board[y+1][x]) <= R:
        DFS(y+1, x)
    if x+1 < N and (y, x+1) not in visited and L <= abs(board[y][x]-board[y][x+1]) <= R:
        DFS(y, x+1)
        

while True:
    checkIfDone = 0
    visited = set()
    for i in range(N):
        for j in range(N):
            unified = set()
            total = 0
            ucnt = 0
            if (i, j) not in visited:
                DFS(i, j)
                if len(unified) == 1:
                    checkIfDone += 1
                    continue
                for y, x, in unified:
                    board[y][x] = total//ucnt

    if checkIfDone == N*N:
        break
    result += 1

    # print(board)

print(result)
