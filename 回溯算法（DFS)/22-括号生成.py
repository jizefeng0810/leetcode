class Solution:
    def generateParenthesis(self, n: int):
        """
            数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
        """
        if n == 0: return []
        res = []
        track = ''
        self.backtrack(n, n, track, res)
        return  res

    def backtrack(self, left, right, track, res):
        if right < left: return
        if left < 0 or right < 0: return
        if left == 0 and right == 0:
            res.append(track)
            return

        track = track + '('
        self.backtrack(left-1, right, track, res)
        track = track[:-1]

        track = track + ')'
        self.backtrack(left, right-1, track, res)
        track = track[:-1]



if __name__=='__main__':
    n = 3   # ['((()))', '(()())', '(())()', '()(())', '()()()']
    solution = Solution()
    result = solution.generateParenthesis(n)
    print(result)
