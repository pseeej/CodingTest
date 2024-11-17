# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node):
        if node is None:
            return

        self.result += 1

        if node.left is not None:
            self.DFS(node.left)
        if node.right is not None:
            self.DFS(node.right)
        


    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        self.DFS(root)
        return self.result
