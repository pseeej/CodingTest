class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxnum = max(nums)

        if maxnum+1 == len(nums):
            return maxnum+1
        return list({i for i in range(maxnum+1)}-set(nums))[0]
