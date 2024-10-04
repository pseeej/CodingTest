import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input().strip()))

def printboard():
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()
    print()


for i in range(N):
    for j in range(N):
        if board[i][j] == 'Y':
            board[i][j] = 1
        else:
            board[i][j] = 0

for i in range(N):
    for j in range(N):
        if not board[i][j]:
            continue

        for k in range(N):
            if board[i][j] == 1 and board[j][k] == 1 and i != k and not board[i][k]:
                board[i][k] = 2

result = 0
for i in range(N):
    result = max(result, N-(board[i].count(0)))

# printboard()

print(result)
