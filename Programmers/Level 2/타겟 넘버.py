def solution(numbers, target):
    global answer
    answer = 0
    
    def DFS(idx, nums, result, target):
        global answer
        if idx == len(nums):
            if result == target:
                answer += 1
            return
        
        DFS(idx+1, nums, result+nums[idx], target)
        DFS(idx+1, nums, result-nums[idx], target)
        
        return
        
    DFS(0, numbers, 0, target)
    
    return answer
