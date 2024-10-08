# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (left+right)//2

        while guess(mid) != 0 and left <= mid:
            # print(left, right, mid)
            result = guess(mid)
            if result == -1:
                right = mid-1
            elif result == 1:
                left = mid+1
            
            mid = (left+right)//2

        return mid
