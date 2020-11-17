class Solution:
    def rob(self, nums) -> int:
        def dp(nums, start):
            if start >= len(nums):
                return 0
            if memo[start] != -1: return memo[start]
            memo[start] = max(dp(nums, start+1), nums[start]+dp(nums,start+2))
            return memo[start]

        memo = [-1] * len(nums)
        return dp(nums, 0)

    def rob_dp(self, nums) -> int:
        n = len(nums)
        dp = [0]*(n+2)
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        return dp[0]



if __name__=='__main__':
    nums = [1,2,3,1]
    solution = Solution()
    result = solution.rob(nums)
    print(result)
    result = solution.rob_dp(nums)
    print(result)
