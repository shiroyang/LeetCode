# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 木のDP
        ans = -10**16

        def get_max_gain(node):
            nonlocal ans
            if node == None: return 0

            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)
            cur_gain = node.val + gain_on_left + gain_on_right
            ans = max(ans, cur_gain)
            return node.val + max(gain_on_left, gain_on_right)
        
        get_max_gain(root)
        return ans