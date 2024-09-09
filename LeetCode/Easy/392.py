class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        stdidx = 0
        while idx < len(t):
            if stdidx >= len(s):
                return True

            if s[stdidx] == t[idx]:
                stdidx += 1
            idx += 1

        if stdidx >= len(s):
            return True

        return False
            
        
