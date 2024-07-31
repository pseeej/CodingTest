class Solution:
    def binSearch(self, nums, target, left, right):
        if left >= right:
            if nums[left] == target:
                return left
            else:
                return -1
        
        mid = (left+right-1)//2
        if target == nums[mid]:
            return mid
        elif nums[left] <= target < nums[mid]:
            return self.binSearch(nums, target, left, mid)
        elif nums[mid] < target <= nums[right-1]:
            return self.binSearch(nums, target, mid+1, right)
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums))
