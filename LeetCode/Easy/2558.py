from math import sqrt
from heapq import heappush, heappop
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heappush(heap, -gift)
        
        lefts = []
        for _ in range(k):
            num = -heappop(heap)
            num = int(sqrt(num))
            heappush(heap, -num)

        result = 0
        for num in heap:
            result += -num

        return result
            
