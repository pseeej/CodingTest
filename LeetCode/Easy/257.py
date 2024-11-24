# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, currnode, currpath):
        if currnode.left is not None:
            self.DFS(currnode.left, currpath+[currnode.left.val])
        if currnode.right is not None:
            self.DFS(currnode.right, currpath+[currnode.right.val])

        if currnode.left is None and currnode.right is None:
            self.result.append('->'.join(map(str, currpath)))

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []

        self.DFS(root, [root.val])

        return self.result
