import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    # DFS 써야징
    next = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = 0
                next.append((i, j))
                while next:
                    y, x = next.popleft()

                    if y > 0 and board[y-1][x] == 1:
                        next.append((y-1, x))
                        board[y-1][x] = 0
                    if x > 0 and board[y][x-1] == 1:
                        next.append((y, x-1))
                        board[y][x-1] = 0
                    if y < N-1 and board[y+1][x] == 1:
                        next.append((y+1, x))
                        board[y+1][x] = 0
                    if x < M-1 and board[y][x+1] == 1:
                        next.append((y, x+1))
                        board[y][x+1] = 0

                cnt += 1
    
    print(cnt)
                
