class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if strx == strx[::-1]:
            return True
        else:
            return False
