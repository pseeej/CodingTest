import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
w_loc = []

for i in range(R):
    line = input()
    for j in range(len(line)):
        if line[j] == 'W':
            w_loc.append((i, j))
    board.append(line)

# .을 그냥 다 울타리라고 생각해보자
# 늑대의 상하좌우 확인하면 되지 않을까
for w in w_loc:
    w_y, w_x = w

    if w_y > 0 and board[w_y-1][w_x] == 'S':    # 상
        print(0)
        exit()
    if w_x > 0 and board[w_y][w_x-1] == 'S':    # 좌
        print(0)
        exit()
    if w_y < R-1 and board[w_y+1][w_x] == 'S':  # 하
        print(0)
        exit()
    if w_x < C-1 and board[w_y][w_x+1] == 'S':  # 우
        print(0)
        exit()

# 늑대랑 양 아니면 걍 다 울타리로 쳐버리기
print(1)
for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            print('D', end="")
        else:
            print(board[i][j], end="")
    print()
