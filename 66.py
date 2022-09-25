class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        realnum = ""
        for i in digits:
            realnum += str(i)
        
        realnum = int(realnum)
        realnum += 1
        
        realnum = str(realnum)
        result = []
        for i in realnum:
            result.append(int(i))
            
        return result
