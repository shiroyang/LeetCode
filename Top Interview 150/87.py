# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        self.trav = []
        def dfs(x):
            if x.left: dfs(x.left)
            self.trav.append(x.val)
            if x.right: dfs(x.right)
        
        dfs(root)
        return self.trav[k-1]