def rotation(arr, query):
    first_x, first_y, last_x, last_y = query
    first_x -= 1
    first_y -= 1
    last_x -= 1
    last_y -= 1
    
    changed = []
   
    temp = arr[first_x][first_y]
    changed.append(temp)
    
    # -> 방향
    for i in range(first_y, last_y):
        temp, arr[first_x][i+1] = arr[first_x][i+1], temp
        changed.append(temp)
    
    # 아래로 내려가는 방향
    for i in range(first_x, last_x):
        temp, arr[i+1][last_y] = arr[i+1][last_y], temp
        changed.append(temp)
    
    # <- 방향
    for i in range(last_y, first_y, -1):
        temp, arr[last_x][i-1] = arr[last_x][i-1], temp
        changed.append(temp)
        
    # 위로 올라가는 방향
    for i in range(last_x, first_x, -1):
        temp, arr[i-1][first_y] = arr[i-1][first_y], temp
        changed.append(temp)
        
    return (arr, min(changed))

def solution(rows, columns, queries):
    answer = []
    
    board = [[(i-1)*columns + j for j in range(1, columns+1)]
             for i in range(1, rows+1)]
    
    for q in queries:
        board, small = rotation(board, q)
        answer.append(small)
    
    return answer
