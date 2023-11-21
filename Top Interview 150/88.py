# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal
        self.trav = []
        def dfs(x):
            if x.left: dfs(x.left)
            self.trav.append(x.val)
            if x.right: dfs(x.right)
        
        dfs(root)
        for i in range(len(self.trav)-1):
            if self.trav[i+1]-self.trav[i] <= 0:
                return False
        
        return True