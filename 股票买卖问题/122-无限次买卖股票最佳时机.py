class Solution:
    """
        多次买卖一支股票
    """
    def maxProfit(self, prices):
        dp_i_0, dp_i_1 = 0, -float('inf')
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0

if __name__=='__main__':
    prices = [7,1,5,3,6,4]  # 7
    # prices = [7,6,4,3,1]    # 0
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)