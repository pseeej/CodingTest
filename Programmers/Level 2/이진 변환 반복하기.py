from collections import deque

def solution(s):
    answer = []
    
    zerocount = 0
    changed = 0
    
    while s != '1':
        newnum = ''
        for c in s:
            if c == '0':
                zerocount += 1
            else:
                newnum += c
                
        numlength = len(newnum)
        
        result = deque()
        while numlength:
            if numlength % 2:
                result.appendleft(1)
            else:
                result.appendleft(0)
                
            numlength //= 2
        
        changed += 1
        
        s = ''
        for num in result:
            s += str(num)
            
            
        # print(newnum, len(newnum), s, zerocount)
        
#         if len(s) < 2:
#             break
        
    answer = [changed, zerocount]
    
    return answer
