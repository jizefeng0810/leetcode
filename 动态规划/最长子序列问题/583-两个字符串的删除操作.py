class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
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

        lcs = dp(word1, 0, word2, 0)
        return m - lcs + n - lcs

if __name__=='__main__':
    word1 = "sea"
    word2 = "eat"   # 2
    solution = Solution()
    result = solution.minDistance(word1, word2)
    print(result)
