def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, k = command
        newarr = array[start-1:end]
        newarr.sort()
        answer.append(newarr[k-1])
    
    return answer
