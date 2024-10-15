class Solution:
    def checkIfCaps(self, chrc):
        if ord(chrc) < 97:
            return True
        
        return False

    def detectCapitalUse(self, word: str) -> bool:

        capscount = 0
        for w in word:
            if self.checkIfCaps(w):
                capscount += 1

        if capscount == 1 and self.checkIfCaps(word[0]):
            return True
        elif capscount == 0:
            return True
        elif capscount == len(word):
            return True

        return False
        
