def printboard(board, n):
    for i in range(n):
        for j in range(i+1):
            print(board[i][j], end=" ")
        print()

def solution(n):
    answer = []
    
    diff = [(1, 0), (0, 1), (-1, -1)]
    
    pyramid = [[0 for _ in range(n)] for _ in range(n)]

    num = 1
    
    y, x = 0, 0
    idx = 0

    while True:
        pyramid[y][x] = num
        num += 1
        
        dy, dx = diff[idx]
        y = y+dy
        x = x+dx
        if(x >= n or y >= n or pyramid[y][x] != 0):
            y = y-dy
            x = x-dx
            idx = (idx+1)%3
            dy, dx = diff[idx]
            y = y+dy
            x = x+dx
            if (x >= n or y >= n or pyramid[y][x] != 0):
                break
            
        
    for i in range(n):
        for j in range(i+1):
            answer.append(pyramid[i][j])
        
    
    
    return answer
