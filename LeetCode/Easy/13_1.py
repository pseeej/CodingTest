class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        tovalues = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        idx = len(s)-1
        while idx > 0:
            if tovalues[s[idx-1]] < tovalues[s[idx]]:
                result += (tovalues[s[idx]] - tovalues[s[idx-1]])
                idx -= 1
            else:
                result += tovalues[s[idx]]

            idx -= 1

        if idx == 0:
            result += tovalues[s[0]]

        return result
