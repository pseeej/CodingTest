class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        origin_xs = set()
        origin_ys = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    origin_ys.add(i)
                    origin_xs.add(j)

        for y in origin_ys:
            matrix[y] = [0 for _ in range(len(matrix[y]))]

        for x in origin_xs:
            for y in range(len(matrix)):
                # print(y, x)
                matrix[y][x] = 0


        
        
