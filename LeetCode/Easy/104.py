# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, curr, currdepth):
        if curr == None:
            return
            
        if curr.left == None:
            self.result = max(self.result, currdepth)
        else:
            self.DFS(curr.left, currdepth+1)

        if curr.right == None:
            self.result = max(self.result, currdepth)
        else:
            self.DFS(curr.right, currdepth+1)

        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        self.DFS(root, 1)
        return self.result
