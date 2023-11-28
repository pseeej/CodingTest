from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    
    scov = []
    for s in scoville:
        heappush(scov, s)
    
    while scov:
        sm1 = heappop(scov)    
        if sm1 >= K:
            break
            
        if len(scov) == 0:
            return -1
        sm2 = heappop(scov)
        
        newcalc = sm1 + (sm2*2)
        heappush(scov, newcalc)
        answer += 1
    
    return answer
