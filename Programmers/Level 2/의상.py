from collections import defaultdict
def solution(clothes):
    answer = 1
    
    weartypes = defaultdict(int)
    for thing, weartype in clothes:
        weartypes[weartype] += 1
        
    for cnt in weartypes.values():
        answer *= (cnt+1)
    answer -= 1
    
    return answer
