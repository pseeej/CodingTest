from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        allnums = [True for _ in range(n)]
        for num in range(2, int(sqrt(n))+1):
            if allnums[num]:
                for idx in range(num+num, n, num):
                    allnums[idx] = False

        return sum(allnums[2:])


        
