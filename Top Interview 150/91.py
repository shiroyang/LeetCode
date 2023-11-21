"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        from collections import deque
        
        que = deque([node])
        clones = {node.val: Node(node.val, [])}

        while que:
            x = que.popleft()
            x_clone = clones[x.val]

            for nx in x.neighbors:
                if nx.val not in clones:
                    clones[nx.val] = Node(nx.val, [])
                    que.append(nx)

                x_clone.neighbors.append(clones[nx.val])
        
        return clones[node.val]