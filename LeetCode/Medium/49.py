## Much Better (Runtime 11ms(beats 80.18%), Memory 19.67MB(beats 80.14%))

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sortedword = ''.join(sorted(word))
            anagrams[sortedword].append(word)

        return list(anagrams.values())



## my original code (Runtime 41ms(beats 8.08%), Memory 24.28MB(beats 10.44%))

from collections import defaultdict
class Solution:
    def countAlphas(self, word):
        alphacnt = defaultdict(int)
        for c in word:
            alphacnt[c] += 1

        # print(tuple(alphacnt.items()))
        return tuple(sorted(tuple(alphacnt.items())))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            cnts = self.countAlphas(word)
            anagrams[cnts].append(word)

        return list(anagrams.values())
        
