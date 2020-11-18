class Solution:
    """
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    """
    def canPartition(self, nums) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0: return False
        sum //= 2
        dp = [False for _ in range(sum+1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(sum, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] | dp[j - nums[i]]
        return dp[sum]

if __name__ == '__main__':
    nums = [1, 5, 11, 5]    # True
    # nums = [1, 2, 3, 5]     # Fasle
    solution = Solution()
    result = solution.canPartition(nums)
    print(result)
