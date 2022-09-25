class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()[-1]
        return len(word)
