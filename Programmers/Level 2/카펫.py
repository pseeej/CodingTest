def solution(brown, yellow):
    answer = []
    
    for y in range(1, brown//2):
        x = brown//2 - y
        print(y, x)
        if yellow == (y-1)*(x-1):
            answer = [x+1, y+1]
            break
    
    return answer
