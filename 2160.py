N = int(input())

boards = []
for _ in range(N):
    board = []
    for _ in range(5):
        board.append(input())
    
    boards.append(board)

diff = 36
left = 0
right = 0
for i in range(N-1):
    for j in range(i+1, N):
        cnt = 0
        for k in range(5*7):
            row = k//7
            col = k%7

            if boards[i][row][col] != boards[j][row][col]:
                cnt += 1

        if cnt < diff :
            diff = cnt
            left = i
            right = j

print(left+1, right+1)
