# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        镜像翻转二叉树
             4
           /   \
          2     7
         / \   / \
        1   3 6   9

             4
           /   \
          7     2
         / \   / \
        9   6 3   1
    """
    def invertTree(self, root):
        if root == None: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
