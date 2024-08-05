class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent = []

        for c in s:
            if c.isalpha() or c.isdigit():
                sent.append(c.lower())
        
        sent = ''.join(sent)
        return sent == sent[::-1]
        
