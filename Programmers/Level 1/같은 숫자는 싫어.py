def solution(arr):
    answer = []
    
    for num in arr:
        if answer and answer[-1] != num:
            answer.append(num)
        elif not answer:
            answer.append(num)
    
    return answer
