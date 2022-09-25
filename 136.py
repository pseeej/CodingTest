class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cntNum = dict()
        for num in nums:
            if num not in cntNum:
                cntNum[num] = 1
            else:
                cntNum[num] += 1
                
        for num in nums:
            if cntNum[num] == 1:
                return num
