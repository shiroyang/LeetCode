# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # [10] -> [5, 15] -> [3, 8, 18] -> [3, 6, 11, 21]
        # 現在のnodeをleafとして、すべての　parents nodes を rootとした総和を持つ
        if not root:
            return 0

        stack = [(root, [root.val])]
        cnt = 0

        while stack:
            node, Acc = stack.pop()
            cnt += Acc.count(targetSum)

            if node.left:
                stack.append((node.left, [node.left.val + x for x in Acc]+[node.left.val]))
            if node.right:
                stack.append((node.right, [node.right.val + x for x in Acc]+[node.right.val]))

        return cnt                
