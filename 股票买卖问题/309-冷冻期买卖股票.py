class Solution:
    """
        卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    """
    def maxProfit(self, prices):
        dp_i_0, dp_i_1 = 0, -float('inf')
        dp_pre_0 = 0
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        return dp_i_0

if __name__=='__main__':
    prices = [1, 2, 3, 0, 2]  # 3
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)