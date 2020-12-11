class Solution:
    def solveSudoku(self, board) -> None:
        """
            编写一个程序，通过填充空格来解决数独问题。
            一个数独的解法需遵循如下规则：
                数字 1-9 在每一行只能出现一次。
                数字 1-9 在每一列只能出现一次。
                数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
                空白格用 '.' 表示。
        """
        return self.backtrack(board, 0, 0)

    def backtrack(self, board, i, j):
        # 穷举到最后一列的话就换到下一行重新开始。
        if j == 9: return self.backtrack(board, i+1, 0)
        # 找到一个可行解，触发 base case
        if i == 9: return True
        # 如果有预设数字，不用我们穷举
        if board[i][j] != '.':
            return self.backtrack(board,i,j+1)
        for ch in '123456789':
            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, i, j, ch):
                continue
            board[i][j] = ch
            # 如果找到一个可行解，立即结束
            if self.backtrack(board,i,j+1):
                return True
            board[i][j] = '.'
        # 穷举完 1~9，依然没有找到可行解，此路不通
        return False

    def isValid(self, board, r, c, n):
        for i in range(9):
            # 判断行是否存在重复
            if board[r][i] == n: return False
            # 判断列是否存在重复
            if board[i][c] == n: return False
            # 判断 3 x 3 方框是否存在重复
            if board[(r/3)*3 + i/3][(c/3)*3 + i%3] == n:
                return False
        return True
