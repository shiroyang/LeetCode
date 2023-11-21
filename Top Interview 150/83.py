# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque, defaultdict
        if not root: return []
        d = defaultdict(list)
        que = deque()
        que.append((root, 0))
        ans = []

        while que:
            node, depth = que.popleft()
            d[depth].append(node.val)
            if node.left: que.append((node.left, depth+1))
            if node.right: que.append((node.right, depth+1))

        for i in range(len(d)):
            ans.append(sum(d[i])/len(d[i]))
        return ans