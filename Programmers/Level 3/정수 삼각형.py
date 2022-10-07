def solution(triangle):
    answer = 0

    untilsum = [[0 for i in range(len(triangle))] for i in range(len(triangle))]
    untilsum[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):   # 높이
        for j in range(len(triangle[i])):    # 가로
            untilsum[i][j] = untilsum[i-1][j] + triangle[i][j]
            if j > 0 and untilsum[i-1][j] < untilsum[i-1][j-1]:
                untilsum[i][j] = untilsum[i-1][j-1] + triangle[i][j]
                
    # print(untilsum)
    answer = max(untilsum[len(triangle)-1])
    return answer
