class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums)-nums.count(nums[0])-nums.count(nums[-1]) > 0:
            return len(nums)-nums.count(nums[0])-nums.count(nums[-1])
        return 0
