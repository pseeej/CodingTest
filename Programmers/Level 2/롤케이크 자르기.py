def solution(topping):
    answer = 0
    
    lefts = dict()
    rights = dict()
    
    for topp in topping:
        if topp in rights:
            rights[topp] += 1
        else:
            rights[topp] = 1
    
    for i in range(1, len(topping)):
        if topping[i-1] not in lefts:
            lefts[topping[i-1]] = 1
        else:
            lefts[topping[i-1]] += 1
            
        if rights[topping[i-1]] == 1:
            rights.pop(topping[i-1])
        else:
            rights[topping[i-1]] -= 1
            
        # print(lefts, rights)
        
        if len(lefts) == len(rights):
            answer += 1
    
    return answer
