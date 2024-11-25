class Solution:
    def DFS(self, currroom):
        for nextroom in self.rooms[currroom]:
            if nextroom in self.visited:
                continue
            else:
                self.visited.add(nextroom)
                self.DFS(nextroom)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms

        self.visited = {0}
        self.DFS(0)
        if len(self.visited) == len(rooms):
            return True

        return False
