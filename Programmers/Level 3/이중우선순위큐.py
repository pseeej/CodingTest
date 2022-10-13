from collections import deque
def solution(operations):
    answer = []
    nums = []
    
    for op in operations:
        # print(nums)
        order, num = op.split()
        if order == "I":
            nums.append(int(num))
            nums.sort()
        elif num == "1" and nums:
            nums.pop()
        elif num == "-1" and nums:
            nums.pop(0)
            
    if nums:
        answer = [nums[-1], nums[0]]
    else:
        answer = [0, 0]
        
    return answer
