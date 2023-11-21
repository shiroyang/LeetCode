# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        que = deque()
        que.append((root, 0))

        trav_order = []

        while que:
            cur, depth = que.popleft()
            if cur is None: continue
            if trav_order:
                top_node, top_depth = trav_order[-1]
                if top_depth == depth:
                    trav_order.pop()
            trav_order.append((cur.val, depth))
            if cur.left:
                que.append((cur.left, depth+1))
            if cur.right:
                que.append((cur.right, depth+1))

        ans = [x[0] for x in trav_order]
        return ans