import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
def DFS(board, y, x, direction):
    # print(y, x)
    global cnt

    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1

    notCleaned = False
    for i in range(1, 5):
        tmpy, tmpx = y+dy[(direction-i)%4], x+dx[(direction-i)%4]
        if 0 <= tmpy < N and 0 <= tmpx < M and board[tmpy][tmpx] == 0:
            y, x, direction = tmpy, tmpx, (direction-i)%4
            notCleaned = True
            break

    if notCleaned:
        DFS(board, y, x, direction)
    elif 0 <= y-dy[direction] < N and 0 <= x-dx[direction] < M and board[y-dy[direction]][x-dx[direction]] != 1:
        DFS(board, y-dy[direction], x-dx[direction], direction)
    else:
        print(cnt)
        return

DFS(board, r, c, d)
