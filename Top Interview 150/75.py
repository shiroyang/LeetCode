# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ls = []

        def dfs(x):
            nonlocal ls
            if not x: return None
            ls.append(x)
            dfs(x.left)
            dfs(x.right)
        
        dfs(root)
        for i in range(len(ls)-1):
            x = ls[i]
            nx = ls[i+1]
            x.left = None
            x.right = nx

        return root        
