import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(board, y, x, H, W):
    if board[y][x] != '#':
        return
    
    board[y][x] = '.'

    if y > 0 and board[y-1][x] == '#':
        DFS(board, y-1, x, H, W)
    if y < H-1 and board[y+1][x] == '#':
        DFS(board, y+1, x, H, W)
    if x > 0 and board[y][x-1] == '#':
        DFS(board, y, x-1, H, W)
    if x < W-1 and board[y][x+1] == '#':
        DFS(board, y, x+1, H, W)

    return 


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        row = input()
        tmp = []
        for r in row:
            tmp.append(r)
        board.append(tmp)

    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == '#':
                cnt += 1
                DFS(board, i, j, H, W)

    print(cnt)
