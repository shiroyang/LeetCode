# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(root):
            cnt = 0
            stack = [(root, root.val)]
            while stack:
                node, cur_max = stack.pop()
                if node.val >= cur_max:
                    cnt += 1
                    cur_max = node.val
                if node.left is not None:
                    stack.append((node.left, cur_max))
                if node.right is not None:
                    stack.append((node.right, cur_max))

            return cnt

        return rec(root)
