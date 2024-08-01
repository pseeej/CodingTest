class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        aidx = 0
        bidx = 0
        acnt = 0

        while acnt <= m and bidx <= n:
            # print(aidx, bidx, acnt)
            if acnt == m and bidx == n:
                break
            elif acnt == m and bidx < n:
                nums1[aidx] = nums2[bidx]
                aidx += 1
                bidx += 1
            elif bidx == n and acnt < m:
                aidx += 1
                acnt += 1
            elif nums1[aidx] <= nums2[bidx]:
                aidx += 1
                acnt += 1
            elif nums1[aidx] > nums2[bidx]:
                nums1[aidx+1:] = nums1[aidx:-1]
                nums1[aidx] = nums2[bidx]
                aidx += 1
                bidx += 1


        
