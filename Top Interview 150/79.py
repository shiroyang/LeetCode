# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.idx = -1
        self.order = []
        def dfs(x):
            if x.left: dfs(x.left)
            self.order.append(x.val)
            if x.right: dfs(x.right)
        dfs(root)
        print(self.order)

    def next(self) -> int:
        self.idx += 1
        return self.order[self.idx]

    def hasNext(self) -> bool:
        if self.idx + 1 < len(self.order):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()