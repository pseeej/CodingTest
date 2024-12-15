# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, currnode, currpath, currsum):
        if currnode is None:
            return

        if currnode.left is None and currnode.right is None:
            if currsum == self.targetSum:
                self.result.append(currpath)
            return

        if currnode.left is not None:
            self.DFS(currnode.left, currpath+[currnode.left.val], currsum+currnode.left.val)
        if currnode.right is not None:
            self.DFS(currnode.right, currpath+[currnode.right.val], currsum+currnode.right.val)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.result = []

        if root is None:
            return self.result
        self.DFS(root, [root.val], root.val)

        return self.result
