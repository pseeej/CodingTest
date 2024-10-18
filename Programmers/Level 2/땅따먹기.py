def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end="\t")
        print()
    print()

def solution(land):
    answer = 0

    results = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    results[-1] = land[-1]
    
    for i in range(len(land)-1, 0, -1):
        for j in range(len(land[0])):
            for k in range(len(land[0])):
                if j == k:
                    continue
                    
                results[i-1][j] = max(results[i-1][j], results[i][k]+land[i-1][j])
                
        # printboard(results)
                

    return max(results[0])
