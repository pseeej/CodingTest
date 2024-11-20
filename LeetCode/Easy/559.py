"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self, currnode, currdepth):
        if currnode is None:
            return

        for child in currnode.children:
            self.DFS(child, currdepth+1)

        if currdepth > self.result:
            self.result = currdepth
        # self.result = max(self.result, currdepth)

        
    def maxDepth(self, root: 'Node') -> int:
        self.result = 0

        if root is None:
            return 0

        self.DFS(root, 1)
        return self.result
