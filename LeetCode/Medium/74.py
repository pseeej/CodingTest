class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lasts = []
        idx = 0
        for idx in range(len(matrix)):
            if matrix[idx][-1] >= target:
                break

        if target in set(matrix[idx]):
            return True

        return False
