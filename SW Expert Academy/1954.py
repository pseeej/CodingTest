T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    limit = N**2

    board = [[0 for _ in range(N)] for _ in range(N)]

    num = 1
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    turn = 0
    wall = 1
    y = wall-1
    x = wall-1

    while num <= limit:
        # print(num, y, x)
        board[y][x] = num

        if turn == 0 and x == N-wall:
            turn += 1
        elif turn == 1 and y == N-wall:
            turn += 1
        elif turn == 2 and x == wall-1:
            turn += 1
        elif turn == 3 and y == wall:
            turn = 0
            wall += 1

        y += dy[turn]
        x += dx[turn]
        num += 1

    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
