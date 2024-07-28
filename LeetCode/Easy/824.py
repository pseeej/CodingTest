class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        results = []

        words = sentence.split()
        for i in range(len(words)):
            newword = ""
            word = words[i]
            if word[0] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                newword = word+"ma"
            else:
                newword = word[1:]
                newword += word[0]
                newword += "ma"

            results.append(newword+"a"*(i+1))
        
        return ' '.join(results)
