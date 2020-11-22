class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        memo = [[-1] * n for _ in range(m)]

        def dp(s1, i, s2, j):
            if i == len(s1) or j == len(s2):
                return 0
            if memo[i][j] != -1:   return memo[i][j]
            if s1[i] == s2[j]:
                memo[i][j] = 1 + dp(s1, i + 1, s2, j + 1)
            else:
                memo[i][j] = max(dp(s1, i + 1, s2, j), dp(s1, i, s2, j + 1))
            return memo[i][j]

        return dp(text1, 0, text2, 0)

if __name__=='__main__':
    word1 = "abcde"
    word2 = "ace"   # 3
    solution = Solution()
    result = solution.longestCommonSubsequence(word1, word2)
    print(result)