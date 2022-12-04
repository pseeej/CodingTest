import copy
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())

newboard = []
islands = []
for i in range(R):
    tmp = ""
    for j in range(C):
        if board[i][j] == "X":
            sea_cnt = 0
            if (i > 0 and board[i-1][j] == ".") or i == 0:
                sea_cnt += 1
            if (j > 0 and board[i][j-1] == ".") or j == 0:
                sea_cnt += 1
            if (i < R-1 and board[i+1][j] == ".") or i == R-1:
                sea_cnt += 1
            if (j < C-1 and board[i][j+1] == ".") or j == C-1:
                sea_cnt += 1

            if sea_cnt >= 3:
                tmp += "."
            else:
                tmp += "X"
                islands.append((i, j))
        else:
            tmp += "."

    newboard.append(tmp)

row_sorted_islands = sorted(islands, key=lambda islands:islands[0])
min_row = row_sorted_islands[0][0]
max_row = row_sorted_islands[-1][0]

col_sorted_islands = sorted(islands, key=lambda islands:islands[1])
min_col = col_sorted_islands[0][1]
max_col = col_sorted_islands[-1][1]

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        print(newboard[i][j], end="")
    print()
