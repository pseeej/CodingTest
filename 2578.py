# 열별로 확인
def checkCol(board):
    cnt = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += board[j][i]
        if tmp == 0:
            cnt += 1

    return cnt

# 행별로 확인
def checkRow(board):
    cnt = 0
    for i in range(5):
        if sum(board[i]) == 0:
            cnt += 1

    return cnt

# 왼쪽 위에서 오른쪽 아래로 내려가는 대각선
def checkAccL(board):
    res = 0
    for i in range(5):
        res += board[i][i]
    
    if res == 0:
        return 1

    return 0

# 오른쪽 위에서 왼쪽 아래로 내려가는 대각선
def checkAccR(board):
    res = 0
    for i in range(5):
        res += board[i][4-i]
    
    if res == 0:
        return 1
        
    return 0

# 해당 값이 있는 위치에 방문 표시해주기
def checkNum(board, num):
    for i in range(5):
        if num in board[i]:
            col = board[i].index(num)
            if board[i][col] > 0 :
                board[i][col] = 0

# 그냥 빙고판 어떻게 그려지나... 확인 위해 만든 함수
def printBoard(board):
    print()

    for i in range(5):
        for j in range(5):
            print("%3d" %board[i][j], end=" ")
        print()

    print()



board = []

for _ in range(5):
    row = list(map(int, input().split()))
    board.append(row)

called = []
for _ in range(5):
    called.append(list(map(int, input().split())))


flag = False
for i in range(5):
    for j in range(5):
        num = called[i][j]
        checkNum(board, num)

        res = checkCol(board) + checkRow(board) + checkAccL(board) + checkAccR(board)

        #print(i*5+j+1)
        #print(checkCol(board), checkRow(board), checkAccL(board), checkAccR(board))
        #printBoard(board)

        if res >= 3:
            print(i*5+j+1)
            flag = True
            break
    
    if flag == True:
        break
2578.py
