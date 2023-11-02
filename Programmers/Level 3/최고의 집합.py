def solution(n, s):
    
    if s < n:
        return [-1]
    
    answer = [s//n for _ in range(n)]
    
    mod = s%n
    
    for i in range(mod):
        answer[-(i+1)] += 1    
    
    return answer
