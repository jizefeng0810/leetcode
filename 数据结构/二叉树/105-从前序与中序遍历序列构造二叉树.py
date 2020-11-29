# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
            根据一棵树的前序遍历与中序遍历构造二叉树。
        """
        return self.bulid(preorder, 0, len(preorder)-1,
                     inorder, 0, len(inorder)-1)

    def bulid(self, preorder, preStart, preEnd,
              inorder, inStart, inEnd):
        if preStart > preEnd: return None
        rootVal = preorder[preStart]
        index = inorder.index(rootVal)

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.bulid(preorder, preStart+1, preStart+leftSize,
                               inorder, inStart, index-1)
        root.right = self.bulid(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index+1, inEnd)
        return root