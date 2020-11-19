class Solution:
    """
        给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
        你可以对一个单词进行如下三种操作：
            插入一个字符
            删除一个字符
            替换一个字符
    """
    def minDistance(self, word1, word2) -> int:
        memo = {}
        def dp(i, j):
            if j == -1: return i + 1
            if i == -1: return j + 1
            if (i,j) in memo.keys():
                return memo[(i,j)]

            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i-1, j-1)
            else:
                memo[(i,j)] = min(
                    dp(i, j-1) + 1,     # 插入
                    dp(i-1, j) + 1,     # 删除
                    dp(i-1, j-1) + 1,   # 替换
                )
            return memo[(i,j)]
        return dp(len(word1)-1, len(word2)-1)

if __name__=='__main__':
    word1 = "horse"
    word2 = "ros"   # 3
    solution = Solution()
    result = solution.minDistance(word1, word2)
    print(result)