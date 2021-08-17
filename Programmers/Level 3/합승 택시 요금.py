def solution(n, s, a, b, fares):
    answer = float("inf")
    
    arr = [[float("inf") for i in range(n+1)] for i in range(n+1)] # 초기화
    
    for fare in fares:
        x, y, z = fare
        arr[x][y] = z
        arr[y][x] = z
        
    for i in range(1, n+1):
        arr[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j]) # 최단 경로 탐색
                
    for i in range(1, n+1):
        res = arr[s][i] # 시작 지점부터 경유 지점까지의 거리
        res += (arr[i][a] + arr[i][b]) # 경유 지점부터 a와 b의 최종 집까지의 거리
        answer = min(res, answer) # 최단 거리 빼내오기
    
    return answer
