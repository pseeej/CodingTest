class Solution:
    def climbStairs(self, n: int) -> int:
        prevs = {1:1, 2:2, 3:3}
        
        for i in range(4, n+1):
            prevs[i] = prevs[i-1]+prevs[i-2]
            
        return prevs[n]
