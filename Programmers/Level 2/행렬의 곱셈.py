def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    M = len(arr1)
    N = len(arr2[0])
    K = len(arr1[0])
    
    print(len(arr1), len(arr2), len(arr1[0]))
    
    for i in range(M):
        for j in range(N):
            for k in range(K):
                answer[i][j] += arr1[i][k]*arr2[k][j]
                # pass
    
    return answer
