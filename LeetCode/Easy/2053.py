from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for alpha in arr:
            counts[alpha] += 1

        onces = set()
        for alpha in counts.keys():
            if counts[alpha] == 1:
                onces.add(alpha)

        if len(onces) < k:
            return ""

        turn = 1
        for alpha in arr:
            if alpha in onces:
                if turn == k:
                    return alpha
                else:
                    turn += 1

        return ""
        
            
