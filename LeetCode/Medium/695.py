class Solution:
    def countAreaSize(self, y, x):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # print(y, x, self.currsize, end=" / ")

        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(self.board) and 0 <= nx < len(self.board[0]) and self.board[ny][nx] == 1:
                self.board[ny][nx] = -1
                self.currsize += 1
                self.countAreaSize(ny, nx)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.board = grid
        result = 0
        self.currsize = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    self.board[i][j] = -1
                    self.currsize = 1
                    self.countAreaSize(i, j)
                    # print()

                if self.currsize > result:
                    result = self.currsize

        return result
        
