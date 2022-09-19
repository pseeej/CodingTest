import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

global board
global w, h

def check_visit(cury, curx):
    # 순서대로 위, 왼쪽, 아래, 오른쪽
    if cury > 0 and board[cury-1][curx] == 1:
        board[cury-1][curx] = 0
        check_visit(cury-1, curx)
    if curx > 0 and board[cury][curx-1] == 1:
        board[cury][curx-1] = 0
        check_visit(cury, curx-1)
    if cury < h-1 and board[cury+1][curx] == 1:
        board[cury+1][curx] = 0
        check_visit(cury+1, curx)
    if curx < w-1 and board[cury][curx+1] == 1:
        board[cury][curx+1] = 0
        check_visit(cury, curx+1)

    # 왼쪽위, 오른쪽아래, 오른쪽위, 왼쪽아래 대각선
    if cury > 0 and curx > 0 and board[cury-1][curx-1] == 1:
        board[cury-1][curx-1] = 0
        check_visit(cury-1, curx-1)
    if cury < h-1 and curx < w-1 and board[cury+1][curx+1] == 1:
        board[cury+1][curx+1] = 0
        check_visit(cury+1, curx+1)
    if cury > 0 and curx < w-1 and board[cury-1][curx+1] == 1:
        board[cury-1][curx+1] = 0
        check_visit(cury-1, curx+1)
    if cury < h-1 and curx > 0 and board[cury+1][curx-1] == 1:
        board[cury+1][curx-1] = 0
        check_visit(cury+1, curx-1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    for i in range(h):
        board.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                continue

            check_visit(i, j)
            cnt += 1
    
    print(cnt)
