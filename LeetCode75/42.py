# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left: return root.right
            if not root.right: return root.left

            # 找到比要删除的节点再大一点点的节点当做下一个parent,来保持平衡状态
            if root.left and root.right: 
                tmp = root.right
                while tmp.left: 
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, root.val)
        return root
