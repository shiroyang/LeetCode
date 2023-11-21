# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []
        que = deque()
        que.append((root, 0))
        order = []
        
        while que:
            node, depth = que.popleft()
            if depth >= len(order):
                order.append([])
            order[depth].append(node.val)

            if node.left: que.append((node.left, depth+1))
            if node.right: que.append((node.right, depth+1))

        return order