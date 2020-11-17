class Solution:
    """
        最多可以完成 k笔 交易。
    """
    def maxProfit(self, max_k, prices):
        def maxProfit_inf(prices):
            dp_i_0, dp_i_1 = 0, -float('inf')
            for i in range(len(prices)):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])
            return dp_i_0

        n = len(prices)
        if max_k > n / 2: return maxProfit_inf(prices)  # k大于最大次数时，与122题无限次无异
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k-1,-1,-1):
                if i - 1 == -1:     # 初始值处理
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k - 1][0];

if __name__=='__main__':
    max_k, prices = 2, [3,2,6,5,0,3]  # 7
    max_k, prices = 2, [2,4,1]  # 2
    max_k, prices = 2, [3,3,5,0,0,3,1,4] # 6
    solution = Solution()
    result = solution.maxProfit(max_k, prices)
    print(result)
