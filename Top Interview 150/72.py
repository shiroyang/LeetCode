# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder starts from root, so we can divide inorder list
        def search(ls):
            nonlocal key
            if not ls: return None
            idx = ls.index(preorder[key])
            root = TreeNode(preorder[key])
            left_ls = ls[:idx]
            right_ls = ls[idx+1:]
            key += 1

            root.left = search(left_ls)
            root.right = search(right_ls)
            
            return root
            
        key = 0
        return search(inorder)