import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
board = []

for _ in range(M):
    tmp = list(map(int, input().split()))
    board.append(tmp)

def DFS(cur_y, cur_x):
    # 상 좌 하 우
    if cur_y > 0 and board[cur_y-1][cur_x] == 1:
        board[cur_y-1][cur_x] = 2
        DFS(cur_y-1, cur_x)
    if cur_x > 0 and board[cur_y][cur_x-1] == 1:
        board[cur_y][cur_x-1] = 2
        DFS(cur_y, cur_x-1)
    if cur_y < M-1 and board[cur_y+1][cur_x] == 1:
        board[cur_y+1][cur_x] = 2
        DFS(cur_y+1, cur_x)
    if cur_x < N-1 and board[cur_y][cur_x+1] == 1:
        board[cur_y][cur_x+1] = 2
        DFS(cur_y, cur_x+1)

    # 왼쪽 위 대각선부터 시계방향
    if cur_y > 0 and cur_x > 0 and board[cur_y-1][cur_x-1] == 1:
        board[cur_y-1][cur_x-1] = 2
        DFS(cur_y-1, cur_x-1)
    if cur_y > 0 and cur_x < N-1 and board[cur_y-1][cur_x+1] == 1:
        board[cur_y-1][cur_x+1] = 2
        DFS(cur_y-1, cur_x+1)
    if cur_y < M-1 and cur_x < N-1 and board[cur_y+1][cur_x+1] == 1:
        board[cur_y+1][cur_x+1] = 2
        DFS(cur_y+1, cur_x+1)
    if cur_y < M-1 and cur_x > 0 and board[cur_y+1][cur_x-1] == 1:
        board[cur_y+1][cur_x-1] = 2
        DFS(cur_y+1, cur_x-1)

    return True

cnt = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = 2
            DFS(i, j)
            cnt += 1

print(cnt)
