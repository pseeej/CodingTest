class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morsecds = dict()
        for i in range(26):
            morsecds[chr(97+i)] = codes[i]

        result = set()
        for word in words:
            tmpcd = ""
            for ch in word:
                tmpcd += morsecds[ch]
            result.add(tmpcd)

        return len(result)
