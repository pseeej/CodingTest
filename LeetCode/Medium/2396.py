from collections import deque
class Solution:
    def change2base(self, num, basenum):
        result = deque()
        while num > 0:
            result.appendleft(num%basenum)
            num //= basenum

        return ''.join(map(str, result))

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            changenum = self.change2base(n, i)
            if changenum != changenum[::-1]:
                return False
        
        return True
