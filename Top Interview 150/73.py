# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder: return None
        # 左右中，pop出来的是中
        cur_val = postorder.pop()
        root = TreeNode(cur_val)
        # 左中右，分割左子树和右子树
        idx = inorder.index(cur_val)            

        right = self.buildTree(inorder[idx+1:], postorder)
        left = self.buildTree(inorder[:idx], postorder)
        root.left = left
        root.right = right

        return root