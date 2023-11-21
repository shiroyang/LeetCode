# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(x):
            if not x: return
            x.left, x.right = x.right, x.left

            invert(x.left)
            invert(x.right)
        
        invert(root)
        return root