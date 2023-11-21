# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        stack = [root]

        while stack:
            cur = stack.pop()
            if not cur:
                return None
            
            if cur.val == val:
                return cur
            elif cur.val > val:
                stack.append(cur.left)
            else:
                stack.append(cur.right)

        
            