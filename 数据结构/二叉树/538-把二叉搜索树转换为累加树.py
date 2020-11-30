# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
    """
    def convertBST(self, root) -> TreeNode:
        self.sum = 0
        self.traverse(root)
        return root

    def traverse(self, root):
        if root == None: return
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)