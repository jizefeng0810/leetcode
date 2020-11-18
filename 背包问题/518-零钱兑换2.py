class Solution:
    """
    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
    """
    def change(self, amount, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        print(dp)
        return dp[amount]

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]    # 4
    solution = Solution()
    result = solution.change(amount, coins)
    print(result)