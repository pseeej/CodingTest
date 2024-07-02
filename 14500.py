import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tetromino = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (1, 1), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], [(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(1, 0), (0, 0), (0, 1), (0, 2)], [(2, 0), (2, 1), (1, 1), (0, 1)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 1), (0, 0), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)], [(2, 0), (1, 0), (1, 1), (0, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)], 
    [(0, 0), (0, 1), (1, 1), (0, 2)], [(1, 0), (1, 1), (0, 1), (1, 2)], [(1, 0), (1, 1), (0, 1), (2, 1)], [(0, 0), (1, 0), (1, 1), (2, 0)]
    ]

result = 0
for i in range(N):
    for j in range(M):
        for tet in tetromino:
            checkIfTrue = True
            for dy, dx in tet:
                if not(0 <= i+dy < N and 0 <= j+dx < M):
                    checkIfTrue = False
                    break
            
            if not checkIfTrue:
                continue

            currsum = 0
            for dy, dx in tet:
                currsum += board[i+dy][j+dx]
            
            result = max(currsum, result)

print(result)
            
