class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        findhead = set()
        for edge in edges:
            v1, v2 = edge
            if v1 not in findhead:
                findhead.add(v1)
            else:
                return v1

            if v2 not in findhead: 
                findhead.add(v2)
            else:
                return v2
