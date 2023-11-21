# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque, defaultdict
        ans = [0, 0]
        que = deque()
        que.append((root, 0))
        trav_order = []
        d = defaultdict(int)

        while que:
            cur, depth = que.pop()
            if not cur: continue
            trav_order.append((cur.val, depth))

            if cur.left:
                que.append((cur.left, depth+1))
            
            if cur.right:
                que.append((cur.right, depth+1))

        for node, depth in trav_order:
            d[depth] += node

        ans = list(sorted(d.items(), key= lambda x: (-x[1], x[0])))

        return ans[0][0]+1