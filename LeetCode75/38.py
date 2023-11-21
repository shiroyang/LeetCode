# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from collections import defaultdict

        parent = defaultdict()
        parent[root] = None

        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)
        
        node1 = p
        tmp1 = []
        while parent[node1]:
            tmp1.append(node1)
            node1 = parent[node1]
        tmp1.append(root)

        node2 = q
        tmp2 = []
        while parent[node2]:
            tmp2.append(node2)
            node2 = parent[node2]
        tmp2.append(root)
        
        tmp2 = set(tmp2)

        for item in tmp1:
            if item in tmp2:
                return item