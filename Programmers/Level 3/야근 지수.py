from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    
    heap = []
    for work in works:
        heappush(heap, -work)
        
    for i in range(n):
        newwork = heappop(heap)
        heappush(heap, newwork+1)
        
    for num in heap:
        if num < 0:
            answer += num**2
    
    return answer
