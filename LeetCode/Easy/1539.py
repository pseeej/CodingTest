class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        tfs = [False for _ in range(2001)]
        for num in arr:
            tfs[num] = True

        for i in range(1, len(tfs)):
            if not tfs[i]:
                k -= 1
                if k == 0:
                    return i

