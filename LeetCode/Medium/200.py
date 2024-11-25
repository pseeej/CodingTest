class Solution:
    def DFS(self, y, x):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in d:
            if 0 <= y+dy < len(self.grid) and 0 <= x+dx < len(self.grid[0]) and self.grid[y+dy][x+dx] == "1":
                self.grid[y+dy][x+dx] = "-1"
                self.DFS(y+dy, x+dx)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.result = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    self.result += 1
                    self.DFS(i, j)

        return self.result
