# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root: return []
        que = deque()
        que.append((root, 0))
        trav = []
        ans = [root.val]

        while que:
            node, depth = que.popleft()
            trav.append((node.val, depth))
            if node.right: que.append((node.right, depth+1))
            if node.left: que.append((node.left, depth+1))
        
        for i in range(len(trav)-1):
            x, depth1 = trav[i]
            nx, depth2 = trav[i+1]
            if depth2 > depth1:
                ans.append(nx)
        
        return ans