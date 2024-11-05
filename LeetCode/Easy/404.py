# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeft(self, node):
        if node.left and node.left.left == None and node.left.right == None:
            self.result += node.left.val

        if node.left:
            self.findLeft(node.left)
        if node.right:
            self.findLeft(node.right)
        

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.findLeft(root)

        return self.result
