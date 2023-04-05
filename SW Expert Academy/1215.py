for test_case in range(1, 11):
    length = int(input())
    board = []
    for _ in range(8):
        board.append(input())

    cnt = 0

    # 가로로 length씩
    for i in range(8):
        for j in range(8-length+1):
            word = board[i][j:j+length]
            if word == word[::-1]:
                cnt += 1

    # 세로로 length씩
    for i in range(8):
        for j in range(8-length+1):
            word = ""
            for k in range(length):
                word += board[j+k][i]
            if word == word[::-1]:
                cnt += 1

    print(f"#{test_case} {cnt}")


