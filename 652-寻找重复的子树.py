class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = {}
        res = []
        def traverse(root):
            if root == None: return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subTree = left + ',' + right + ',' + str(root.val)
            if subTree not in memo.keys():
                memo[subTree] = 0
            else:
                memo[subTree] = memo[subTree] + 1
            if memo[subTree] == 1:  # 防止重复添加
                res.append(root)
            return subTree
        traverse(root)
        return res