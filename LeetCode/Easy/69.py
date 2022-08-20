class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        for i in range(1, x//2+2):
            if i*i <= x:
                res = i
            if i*i > x:
                break
                
        return res
