def solution(nums):
    answer = 0
    
    canget = len(nums)//2
    if len(set(nums)) >= canget:
        return canget
    else:
        return len(set(nums))
    
    return answer
