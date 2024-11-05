class Solution:
    def DFS(self, y, x):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if (ny, nx) not in self.visited and 0 <= ny < len(self.image) and 0 <= nx < len(self.image[0]) and self.image[ny][nx] == self.orgclr:
                self.image[ny][nx] = self.newclr
                self.visited.add((ny, nx))
                self.DFS(ny, nx)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.orgclr = image[sr][sc]
        self.image = image
        self.newclr = color
        
        self.visited = {(sr, sc)}
        self.image[sr][sc] = self.newclr

        self.DFS(sr, sc)

        return self.image
