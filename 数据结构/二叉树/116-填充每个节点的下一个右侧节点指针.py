"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
        给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。
        填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
    """
    def connect(self, root):
        if root == None: return None
        self.connectTwoNode(root.left, root.right)
        return root

    def connectTwoNode(self, node1, node2):
        if node1 == None or node2 == None: return
        node1.next = node2
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node1.right, node2.left)
        self.connectTwoNode(node2.left, node2.right)
