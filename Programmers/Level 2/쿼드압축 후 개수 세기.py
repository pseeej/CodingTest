def solution(arr):
    answer = [0, 0]
    
    length = len(arr)
    
    while length >= 1:
        starts = [] # 시작 포인트들 저장해둔 리스트
        for i in range(0, len(arr), length):
            for j in range(0, len(arr), length):
                starts.append((i, j))
        
        for start in starts:
            y, x = start
            tmpsum = 0
            
            # 이미 압축 완료된 칸이면 건너뛰기
            if arr[y][x] == 'X':
                continue
            
            for i in range(y, y+length):
                tmpsum += sum(arr[i][x:x+length])
                
            # 각 칸의 값이 모두 1이면
            if tmpsum == length*length:
                for i in range(y, y+length):
                    for j in range(x, x+length):
                        arr[i][j] = 'X'
                        
                answer[1] += 1
                
            # 각 칸의 값이 모두 0이면
            elif tmpsum == 0:
                for i in range(y, y+length):
                    for j in range(x, x+length):
                        arr[i][j] = 'X'
                        
                answer[0] += 1
        
        length //= 2
    
    return answer
