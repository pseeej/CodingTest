import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
board = []

def printboard(board, R, C):
    for i in range(R):
        for j in range(C):
            if board[i][j] != '.':
                print('O', end="")
            else:
                print('.', end="")
        print()
    

for _ in range(R):
    board.append(list(input().strip()))

for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            board[i][j] = 0

# printboard(board, R, C)

time = 2
while time <= N:
    if time%2 == 1: # 3초 전 폭탄 터짐
        for y in range(R):
            for x in range(C):
                if board[y][x] == time-3:
                    board[y][x] = '.'
                    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dy, dx in d:
                        ny = dy+y
                        nx = dx+x
                        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != time-3:
                            board[ny][nx] = '.'

    else:
        for y in range(R):
            for x in range(C):
                if board[y][x] == '.':
                    board[y][x] = time

    time += 1

    # printboard(board,R, C)
    # print()


printboard(board, R, C)
                    
        
        
        
    
