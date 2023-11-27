import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, data, depth=1):
        self.data = data
        self.left = None
        self.right = None
        self.depth = depth

def build_tree(indexes):
    from collections import deque
    root = Node(1)
    queue = deque([root])

    for left, right in indexes:
        current = queue.popleft()
        if left != -1:
            current.left = Node(left, current.depth + 1)
            queue.append(current.left)
        if right != -1:
            current.right = Node(right, current.depth + 1)
            queue.append(current.right)

    return root

def in_order_traversal(node):
    return in_order_traversal(node.left) + [node.data] + in_order_traversal(node.right) if node else []

def swap_at_depth(node, k):
    if node:
        if node.depth % k == 0:
            node.left, node.right = node.right, node.left
        swap_at_depth(node.left, k)
        swap_at_depth(node.right, k)

def swapNodes(indexes, queries):
    root = build_tree(indexes)
    result = []

    for k in queries:
        swap_at_depth(root, k)
        result.append(in_order_traversal(root))

    return result

# Example usage:
indexes = [[2, 3], [-1, -1], [-1, -1]]  # Replace with the actual indexes
queries = [1, 1]  # Replace with the actual queries
print(swapNodes(indexes, queries))
