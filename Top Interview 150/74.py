"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        if not root: return None

        que = deque()
        que.append((root, 0))
        ls = []

        while que:
            cur, depth = que.popleft()
            ls.append((cur, depth))
            if cur.left:
                que.append((cur.left, depth+1))
            if cur.right:
                que.append((cur.right, depth+1))
            
        for i in range(len(ls)-1):
            x, depth1 = ls[i]
            nx, depth2 = ls[i+1]

            if depth1 != depth2: continue
            x.next = nx

        return root