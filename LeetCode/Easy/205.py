class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordmap = dict()

        for i in range(len(s)):
            w1 = s[i]
            if w1 in wordmap and wordmap[w1] != t[i]:
                return False
            elif w1 not in wordmap and t[i] in wordmap.values():
                return False
            elif w1 not in wordmap:
                wordmap[w1] = t[i]


        return True
