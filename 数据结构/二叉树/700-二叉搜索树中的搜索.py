# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回
    """
    def searchBST(self, root, val):
        if root == None: return None
        if root.val == val: return root
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)