# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    """
    def kthSmallest(self, root, k):
        self.list = []
        self.traverse(root)
        return self.list[k-1]

    def traverse(self, root):
        if root == None:
            # self.list.append(None)    # None直接跳过，方便直接输出第k个最小元素
            return
        self.traverse(root.left)
        self.list.append(root.val)
        self.traverse(root.riight)
        return