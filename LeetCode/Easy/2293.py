class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n != 1:
            newnums = []
            for i in range(0, n, 2):
                if (i//2) % 2 == 0:
                    if nums[i] > nums[i+1]:
                        newnums.append(nums[i+1])
                    else:
                        newnums.append(nums[i])
                else:
                    if nums[i] > nums[i+1]:
                        newnums.append(nums[i])
                    else:
                        newnums.append(nums[i+1])

            nums = newnums
            n = len(nums)

        return nums[0]
