from collections import defaultdict
class Solution:
    def DFS(self, currnode):
        for nextnode in self.graph[currnode]:
            if nextnode not in self.visited:
                self.visited.add(nextnode)
                self.DFS(nextnode)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = defaultdict(list)

        for edge in edges:
            v1, v2 = edge
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

        self.visited = set()
        self.visited.add(source)
        self.DFS(source)

        if destination not in self.visited:
            return False
        else:
            return True
