class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = dict()

        for i in range(len(nums)):
            if nums[i] in indices:
                if i-indices[nums[i]] <= k:
                    return True
            indices[nums[i]] = i

        return False
