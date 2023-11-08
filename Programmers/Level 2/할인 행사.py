def solution(want, number, discount):
    answer = 0
        
    jh_wants = dict()
    for i in range(len(want)):
        jh_wants[want[i]] = number[i]
        
    for i in range(len(discount)-sum(number)+1):
        count_days = dict()
        for w in want:
            count_days[w] = 0
            
        for j in range(i, i+sum(number)):
            if discount[j] not in set(want):
                continue
            count_days[discount[j]] += 1
            
        if count_days == jh_wants:
            answer += 1
            
    
    return answer
