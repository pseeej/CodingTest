import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

results = [0, 0]

for i in range(N):
    seroPoss = 0
    garoPoss = 0
    
    for j in range(N):
        if board[i][j] == '.':
            garoPoss += 1
        elif board[i][j] == 'X':
            if garoPoss >= 2:
                results[0] += 1
            garoPoss = 0

        if board[j][i] == '.':
            seroPoss += 1
        elif board[j][i] == 'X':
            if seroPoss >= 2:
                results[1] += 1
            seroPoss = 0

    if garoPoss >= 2:
        results[0] += 1
    if seroPoss >= 2:
        results[1] += 1

print(results[0], results[1])
        
