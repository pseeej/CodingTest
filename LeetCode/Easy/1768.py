class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            std = word1
            longer = word2
        else:
            std = word2
            longer = word1

        result = ""
        for i in range(len(std)):
            result += word1[i] + '' + word2[i]

        result += ''.join(longer[len(std):])
        return result
