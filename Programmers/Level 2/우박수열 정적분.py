def solution(k, ranges):
    answer = []
    
    collatz = [k]
    while k != 1:
        if k%2 == 0:
            k //= 2
        else:
            k = k*3+1
        
        collatz.append(k)
    
    woobak = []
    for i in range(len(collatz)-1):
        a, b = collatz[i], collatz[i+1]
        woobak.append(min(a, b)+(max(a, b)-min(a,b))*1/2)
    
    # print(woobak)
    
    for rang in ranges:
        start, end = rang[0], rang[1]
        end = len(woobak)+end
        
        if end < start:
            answer.append(-1.0)
            continue
        
        result = 0.0
        for i in range(start, end):
            result += woobak[i]
        answer.append(result)
        
    
    return answer
