from copy import deepcopy
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        newarr = []
        for i in range(len(score)):
            newarr.append((score[i], i))

        newarr = sorted(newarr, key=lambda k:k[0], reverse=True)

        result = ["" for _ in range(len(score))]
        for i in range(len(newarr)):
            if i == 0:
                result[newarr[i][1]] = "Gold Medal"
            elif i == 1:
                result[newarr[i][1]] = "Silver Medal"
            elif i == 2:
                result[newarr[i][1]] = "Bronze Medal"
            else:
                result[newarr[i][1]] = str(i+1)

        return result

        return newarr
