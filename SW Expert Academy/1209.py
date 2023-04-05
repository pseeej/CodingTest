size = 100

for _ in range(10):
    test_case = int(input())
    board = []
    for _ in range(size):
        board.append(list(map(int, input().split())))

    result = 0

    # 행별 최댓값
    for i in range(size):
        result = max(result, sum(board[i]))

    # 열별 최댓값
    for i in range(size):
        tmpsum = 0
        for j in range(size):
            tmpsum += board[j][i]

        result = max(result, tmpsum)

    # 대각선별 최댓값
    tmpsum = 0
    for i in range(size):
        tmpsum += board[i][i]

    result = max(result, tmpsum)

    tmpsum = 0
    for i in range(size):
        tmpsum += board[i][size-1-i]

    result = max(result, tmpsum)

    print(f"#{test_case} {result}")
