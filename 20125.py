import sys
input = sys.stdin.readline

N = int(input())
board = []

for _ in range(N):
    board.append(input().strip())

heart = []
for i in range(1, N-1):
    for j in range(1, N-1):
        if board[i][j] == '*' and board[i+1][j] == '*' and board[i-1][j] == '*' and board[i][j+1] == '*' and board[i][j-1] == '*':
            heart = [i, j]
            break
    if len(heart) == 2:
        break

print(heart[0]+1, heart[1]+1)

result = [0 for _ in range(5)]

# 왼쪽 팔
y, x = heart[0], heart[1]
while 0 <= y < N and 0 <= x-1 < N and board[y][x-1] == '*':
    result[0] += 1
    x -= 1

# 오른쪽 팔
y, x = heart[0], heart[1]
while 0 <= y < N and 0 <= x+1 < N and board[y][x+1] == '*':
    result[1] += 1
    x += 1

# 허리
y, x = heart[0], heart[1]
while 0 <= y+1 < N and 0 <= x < N and board[y+1][x] == '*':
    result[2] += 1
    y += 1

hy, hx = y, x
# 왼쪽 다리
y, x = hy, hx-1
while 0 <= y+1 < N and 0 <= x < N and board[y+1][x] == '*':
    result[3] += 1
    y += 1

# 오른쪽 다리
y, x = hy, hx+1
while 0 <= y+1 < N and 0 <= x < N and board[y+1][x] == '*':
    result[4] += 1
    y += 1


for i in range(5):
    print(result[i], end=" ")
    
