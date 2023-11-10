def solution(n):
    answer = []
    
    def hanoii(pan, start, end, mid):
        if pan == 1:
            answer.append([start, end])
            return
        
        hanoii(pan-1, start, mid, end)
        answer.append([start, end])
        hanoii(pan-1, mid, end, start)
        
    hanoii(n, 1, 3, 2)
    
    return answer
