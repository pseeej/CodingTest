class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        worddict = dict()
        svalue = s.split()

        if len(pattern) != len(svalue):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in worddict:
                if svalue[i] not in set(worddict.values()):
                    worddict[pattern[i]] = svalue[i]
                else:
                    return False
            elif worddict[pattern[i]] != svalue[i]:
                return False
        
        return True
