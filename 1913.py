N = int(input())
num = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

def printboard():
    global N, board
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


minn = -1
maxx = N

row = 0
col = 0
curr = N**2

# 0이면 아래, 1이면 오른쪽, 2면 위, 3이면 왼쪽으로 가는 방향이라고 생각하기
way = 0

res1, res2 = 0, 0

while curr > 0:
    board[row][col] = curr

    if curr == num:
        res1 = row + 1
        res2 = col + 1

    # print(row, col, curr)

    if way == 0:
        row += 1
        if row == maxx:
            row -= 1
            col += 1
            way = 1
    elif way == 1:
        col += 1
        if col == maxx:
            col -= 1
            row -= 1
            way = 2
            maxx -= 1
    elif way == 2:
        row -= 1
        if row == minn:
            row += 1
            col -= 1
            way = 3
            minn += 1
    else:
        col -= 1
        if col == minn:
            col += 1
            row += 1
            way = 0
    
    curr -= 1

    

    
printboard()
print(res1, res2)
