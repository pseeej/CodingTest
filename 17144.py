from copy import deepcopy
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(map(int, input().split())))

cleaner = []
for i in range(R):
    if board[i][0] == -1:
        cleaner.append((i, 0))

newboard = deepcopy(board)
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    for y in range(R):
        for x in range(C):
            if board[y][x] <= 0:
                continue

            for dy, dx in diff:
                if 0 <= y+dy < R and 0 <= x+dx < C and board[y+dy][x+dx] != -1:
                    newboard[y+dy][x+dx] += board[y][x]//5
                    newboard[y][x] -= board[y][x]//5

    # 회전하는 부분 만들어야 함!!
    # 윗바퀴
    y, x = cleaner[0]
    cleanup = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dirrup = 0
    prev = newboard[y][x]
    
    while True:
        cury, curx = y+cleanup[dirrup][0], x+cleanup[dirrup][1]
        if not (0 <= cury < R and 0 <= curx < C):
            dirrup += 1
            cury, curx = y+cleanup[dirrup][0], x+cleanup[dirrup][1]
            
        if newboard[cury][curx] == -1 :
            break
        
        if prev == -1:
            prev = 0
        prev, newboard[cury][curx] = newboard[cury][curx], prev
        y, x = cury, curx

    # 아랫바퀴
    y, x = cleaner[1]
    cleandown = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirrdown = 0
    prev = newboard[y][x]
    
    while True:
        cury, curx = y+cleandown[dirrdown][0], x+cleandown[dirrdown][1]
        if not (0 <= cury < R and 0 <= curx < C):
            dirrdown += 1
            cury, curx = y+cleandown[dirrdown][0], x+cleandown[dirrdown][1]
            
        if newboard[cury][curx] == -1:
            break
        
        if prev == -1:
            prev = 0
        prev, newboard[cury][curx] = newboard[cury][curx], prev
        y, x = cury, curx

    board = deepcopy(newboard)

result = 0
for i in range(R):
    for j in range(C):
        # print(board[i][j], end=" ")
        if board[i][j] != -1:
            result += board[i][j]
    # print()
    
print(result)
        
        
            


                
