class Solution:
    def Merge(self, nums, left, mid, right):
        arr = []
        low = left
        high = mid+1

        while low <= mid+1 and high <= right+1:
            if low == mid+1 and high == right+1:
                break
            elif low == mid+1 and high <= right:
                arr.append(nums[high])
                high += 1
            elif high == right+1 and low <= mid:
                arr.append(nums[low])
                low += 1
            elif nums[low] < nums[high]:
                arr.append(nums[low])
                low += 1
            elif nums[low] >= nums[high]:
                arr.append(nums[high])
                high += 1
            else:
                break

        for i in range(len(arr)):
            nums[i+left] = arr[i]

        # print(nums, arr, left, right, mid)

    def MergeSort(self, nums, left, right):
        if left >= right:
            return 

        mid = (left+right)//2
        self.MergeSort(nums, left, mid)
        self.MergeSort(nums, mid+1, right)
        self.Merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.MergeSort(nums, 0, len(nums)-1)
        
        return nums
