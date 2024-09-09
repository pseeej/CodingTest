from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        origindict = defaultdict(int)
        newdict = defaultdict(int)

        for ch in s:
            origindict[ch] += 1
        
        for ch in t:
            newdict[ch] += 1

        if origindict == newdict:
            return True
        return False
        
