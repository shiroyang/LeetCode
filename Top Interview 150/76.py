# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Use dfs to preserve all the sum to leaf
        if not root: return False
        PathSum = set()

        def dfs(x, cur_sum):
            nonlocal PathSum
            cur_sum += x.val
            if x.left == None and x.right == None:
                PathSum.add(cur_sum)
            if x.left: dfs(x.left, cur_sum)
            if x.right: dfs(x.right, cur_sum)
            cur_sum -= x.val
        
        dfs(root, 0)
        return True if targetSum in PathSum else False