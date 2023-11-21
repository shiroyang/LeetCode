# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # (node, is_left, depth)
        # is_left means it can go left side.
        stack = [(root, True, 0), (root, False, 0)]

        while stack:
            cur, is_left, depth = stack.pop()
            ans = max(ans, depth)
            if cur is None: continue
    
            if is_left:
                if cur.left:
                    stack.append((cur.left, False, depth + 1))
                if cur.right:
                    stack.append((cur.right, True, 1))
            else:
                if cur.right:
                    stack.append((cur.right, True, depth + 1))
                if cur.left:
                    stack.append((cur.left, False, 1))

        return ans