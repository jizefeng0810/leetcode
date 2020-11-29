# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, postorder, inorder):
        """
            根据一棵树的中序遍历与后序遍历构造二叉树。
        """
        return self.bulid(postorder, 0, len(postorder)-1,
                     inorder, 0, len(inorder)-1)

    def bulid(self, postorder, postStart, postEnd,
              inorder, inStart, inEnd):
        if inStart > inEnd: return None
        rootVal = postorder[postEnd]
        index = inorder.index(rootVal)

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.bulid(postorder, postStart, postStart+leftSize-1,
                               inorder, inStart, index-1)
        root.right = self.bulid(postorder, postStart+leftSize, postEnd-1,
                                inorder, index+1, inEnd)
        return root