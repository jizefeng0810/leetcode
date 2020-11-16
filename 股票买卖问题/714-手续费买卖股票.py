class Solution:
    """
        买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
    """
    def maxProfit(self, prices, fee):
        dp_i_0, dp_i_1 = 0, -float('inf')
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i] - fee)
        return dp_i_0

if __name__=='__main__':
    prices = [1, 3, 2, 8, 4, 9]  # 8
    fee = 2
    solution = Solution()
    result = solution.maxProfit(prices, fee)
    print(result)