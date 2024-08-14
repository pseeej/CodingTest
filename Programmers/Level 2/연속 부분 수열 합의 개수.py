def solution(elements):
    answer = 0
    sumsets = set()
    length = len(elements)
    elements.extend(elements)
    
    sums = [0 for _ in range(len(elements)+1)]
    for i in range(len(elements)):
        sums[i+1] = sums[i]+elements[i]
        
    # print(sums)
    for i in range(length):
        for j in range(i+1, length+i+1):
            # print(sums[j]-sums[i])
            sumsets.add(sums[j]-sums[i])
    
    # print(sumsets)
    answer = len(sumsets)
    
    return answer
