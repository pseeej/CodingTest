import sys
input = sys.stdin.readline

N = int(input())
board = [True for _ in range(10000001)]
board[0] = False
board[1] = False

for i in range(2, 10000001):
    if board[i] == True:
        idx = i+i
        while idx < 10000001:
            board[idx] = False
            idx += i


cnt = 0
for i in range(len(board)):
    if board[i] == True and cnt == N-1:
        print(i)
        exit()
        
    if board[i] == True:
        cnt += 1
