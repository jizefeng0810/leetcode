class Solution:
    """
        房子不是一排，而是围成了一个圈，环形
    """
    def rob(self, nums) -> int:
        def dp(nums, start, end):
            dp_i, dp_i_1, dp_i_2 = 0, 0, 0
            for i in range(end, start-1, -1):
                dp_i = max(dp_i_1, nums[i] + dp_i_2)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i

        n = len(nums)
        if n == 1: return nums[0]
        return max(dp(nums, 0, n-2), dp(nums, 1, n-1))



if __name__=='__main__':
    nums = [2,3,2]      # 3
    nums = [1,2,3,1]    # 4
    solution = Solution()
    result = solution.rob(nums)
    print(result)
