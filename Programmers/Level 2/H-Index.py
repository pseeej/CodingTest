from collections import defaultdict
def solution(citations):
    answer = 0
    
    refcnt = defaultdict(int)
    
    for cit in citations:
        refcnt[cit] += 1
        
    maxkey = max(refcnt.keys())
    refsum = [0 for _ in range(maxkey+1)]
    for i in range(maxkey+1):
        refsum[i] = refcnt[i]
        
    for i in range(maxkey, 0, -1):
        refsum[i-1] += refsum[i]
        
    for i in range(maxkey, -1, -1):
        if i <= refsum[i]:
            return i
    
    return answer
