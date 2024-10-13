from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        starts = defaultdict(int)
        ends = defaultdict(int)

        for tr in trust:
            start, end = tr
            starts[start] += 1
            ends[end] += 1

        for person in range(1, n+1):
            if ends[person] == n-1 and starts[person] == 0:
                return person

        return -1
