# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        Path = []
        if not root: return 0

        def dfs(x, cur_path):
            nonlocal Path
            cur_path.append(x.val)
            if x.left == None and x.right == None:
                Path.append(cur_path.copy())
            if x.left: dfs(x.left, cur_path)
            if x.right: dfs(x.right, cur_path)
            cur_path.pop()
        
        dfs(root, [])
        ans = 0
        for ls in Path:
            tmp = 0
            for num in ls:
                tmp = tmp * 10 + num
            ans += tmp
        
        return ans