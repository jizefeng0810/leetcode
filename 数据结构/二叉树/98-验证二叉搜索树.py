# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    """
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST(root, None, None)

    def is_ValidBST(self, root, min, max):
        if root == None: return True
        if min != None and root.val <= min.val: return False
        if max != None and root.val >= max.val: return False
        return self.is_ValidBST(root.left, min, root) and self.is_ValidBST(root.right, root, max)