class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = 200
        for i in range(len(strs)):
            if minlength > len(strs[i]):
                minlength = len(strs[i])
            
        res = ""
        for i in range(minlength):
            letter = strs[0][i]
            flag = 1
            for j in range(1, len(strs)):
                if strs[j][i] != letter:
                    flag = 0
                    break
            if flag == 0:
                break
            else:
                res += letter
                
        
        return res
