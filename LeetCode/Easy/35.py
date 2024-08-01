class Solution:
    def binSearch(self, nums, target, left, right):
        if right-left == 1:
            return left+1
        if nums[left] == target:
            return left

        mid = (left+right)//2

        if nums[left] <= target <= nums[mid]:
            return self.binSearch(nums, target, left, mid)
        elif nums[mid] <= target <= nums[right]:
            return self.binSearch(nums, target, mid, right)    

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        return self.binSearch(nums, target, 0, len(nums)-1)
