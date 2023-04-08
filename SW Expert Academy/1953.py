from collections import deque

T = int(input())

move = [(0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)]

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    nextarr = deque()
    nextarr.append((R, C))
    nowcnt = len(nextarr)
    already = set()
    already.add((R, C))
    result = 0

    L -= 1

    while L:
        L -= 1
        nextcnt = 0
        while nowcnt:
            nowcnt -= 1
            y, x = nextarr.popleft()

            if move[board[y][x]][0] == 1 and y > 0 and (y-1, x) not in already and move[board[y-1][x]][2] == 1:
                nextarr.append((y-1, x))
                already.add((y-1, x))
                nextcnt += 1
            if move[board[y][x]][1] == 1 and x < M-1 and (y, x+1) not in already and move[board[y][x+1]][3] == 1:
                nextarr.append((y, x+1))
                already.add((y, x+1))
                nextcnt += 1
            if move[board[y][x]][2] == 1 and y < N-1 and (y+1, x) not in already and move[board[y+1][x]][0] == 1:
                nextarr.append((y+1, x))
                already.add((y+1, x))
                nextcnt += 1
            if move[board[y][x]][3] == 1 and x > 0 and (y, x-1) not in already and move[board[y][x-1]][1] == 1:
                nextarr.append((y, x-1))
                already.add((y, x-1))
                nextcnt += 1

        nowcnt = nextcnt

    print(f"#{test_case} {len(already)}")
