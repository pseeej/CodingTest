def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        if idx//n >= idx%n:
            answer.append(idx//n+1)
        else:
            answer.append(idx%n+1)
    
    return answer
