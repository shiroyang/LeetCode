# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(x):
            if x == None: return 0
            self.cnt += 1
            if x.left: dfs(x.left)
            if x.right: dfs(x.right)
        dfs(root)
        return self.cnt
        