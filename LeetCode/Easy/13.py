class Solution:
    def romanToInt(self, s: str) -> int:
        rom2int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        result = 0
        
        flag = 0
        i = 0
        for i in range(len(s)-1):
            if flag == 1:
                flag = 0
            else:
                if rom2int[s[i]] >= rom2int[s[i+1]]:
                    result += rom2int[s[i]]
                    print(rom2int[s[i]])
                else:
                    result += (rom2int[s[i+1]] - rom2int[s[i]])
                    print(rom2int[s[i+1]]-rom2int[s[i]])
                    flag = 1
                
        if len(s) == 1:
            result += rom2int[s[0]]
        if i==(len(s)-2) and flag == 0:
            result += rom2int[s[-1]]
            
        return result
        
