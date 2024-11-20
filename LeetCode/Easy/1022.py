# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, currnode, currbin):
        if currnode is None:
            return

        if currnode.left is not None:
            self.DFS(currnode.left, currbin+[currnode.left.val])
        if currnode.right is not None:
            self.DFS(currnode.right, currbin+[currnode.right.val])

        if currnode.left is None and currnode.right is None:
            binnum = ''.join(map(str, currbin))
            binint = int(binnum, 2)
            self.result += binint


        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        if root is None:
            return 0

        self.DFS(root, [root.val])

        return self.result
