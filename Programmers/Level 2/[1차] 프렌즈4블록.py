def solution(m, n, board):
    answer = 0
    
    newboard = []
    for b in board:
        newboard.append(list(b))
        
    board = newboard
    
    d = [(-1, 0), (0, 1), (-1, 1)]
    while True:
        goingpopped = set()
        
        # 블록 짝 구해서 터질 애들 구하기
        for y in range(m-1, 0, -1):
            for x in range(n-1):
                if board[y][x] == '.':
                    continue
                    
                std = board[y][x]
                checkIfPop = True
                for dy, dx in d:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == std:
                        continue
                    else:
                        checkIfPop = False
                        break
                        
                if checkIfPop:
                    goingpopped.add((y, x))
                    for dy, dx in d:
                        ny, nx = y+dy, x+dx
                        goingpopped.add((ny, nx))
                          
        # print(goingpopped)
        answer += len(goingpopped)
        
        
        # set에 있는 값들 . 처리로 지워주기
        for y in range(m):
            for x in range(n):
                if (y, x) in goingpopped:
                    board[y][x] = '.'
                
                
        # print(board)
        
        
        # 점 찍은 곳 기준으로 위에서 값 내려오기
        checkIfChanged = False
        
        for y in range(m-1, -1, -1):
            for x in range(n):
                if board[y][x] == '.':
                    tmpy = y
                    while tmpy >= 0 and board[tmpy][x] == '.':
                        tmpy -= 1
                        
                    if tmpy == -1:
                        continue
                    else:
                        board[y][x], board[tmpy][x] = board[tmpy][x], board[y][x]
                        checkIfChanged = True
             
        # print(board)
        
        if checkIfChanged == False:
            break
                
    return answer
