
class Solution:
    """
        给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
        请你返回让 s 成为回文串的 最少操作次数 。
    """
    def minInsertions(self, s) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]

if __name__=='__main__':
    s = "zzazz"     # 0
    # s = "mbadm"     # 2
    solution = Solution()
    result = solution.minInsertions(s)
    print(result)
