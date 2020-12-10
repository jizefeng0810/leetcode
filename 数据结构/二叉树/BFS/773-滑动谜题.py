class Solution:
    """
        在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
        一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
        最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
        给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
    """
    def slidingPuzzle(self, board):
        m, n = 2, 3
        start, target = '', '123450'
        for i in range(m):  # 将 2x3 的数组转化成字符串
            for j in range(n):
                start = start + str(board[i][j])

        # 记录一维字符串的相邻索引
        neighbor = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2],
        ]

        # BFS
        q = []
        visited = set()
        q.append(start)
        visited.add(start)

        step = 0
        while len(q) != 0:
            for i in range(len(q)):
                cur = q.pop(0)
                if target == cur:  # 判断是否达到目标局面
                    return step

                # 找到数字 0 的索引
                idx = 0
                for c in cur:
                    if c != '0':
                        idx += 1
                    else:
                        break

                # 将数字 0 和相邻的数字交换位置
                for adj in neighbor[idx]:
                    new_board = cur
                    if adj < idx:
                        new_board = new_board[:adj] + new_board[idx] + new_board[adj + 1:idx] + new_board[
                            adj] + new_board[idx + 1:]
                    else:
                        new_board = new_board[:idx] + new_board[adj] + new_board[idx + 1:adj] + new_board[
                            idx] + new_board[adj + 1:]
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)
            step += 1
        return -1


if __name__ == '__main__':
    board = [[1, 2, 3], [4, 0, 5]]  # 1
    board = [[1, 2, 3], [5, 4, 0]]  # -1
    # board = [[4, 1, 2], [5, 0, 3]]  # 5
    # board = [[3, 2, 4], [1, 5, 0]]  # 14
    solution = Solution()
    result = solution.slidingPuzzle(board)
    print(result)
