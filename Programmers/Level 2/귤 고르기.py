from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    
    t_cnts = defaultdict(int)
    for t in tangerine:
        t_cnts[t] += 1
        
    nums = list(t_cnts.values())
    nums.sort()
    # print(nums)
    
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    # print(nums)
    
    length = 1
    while True:
        if length >= len(nums):
            break
            
        if(nums[-1]-nums[-1-length]) < k:
            length += 1
        else:
            break
                
    
    return length
