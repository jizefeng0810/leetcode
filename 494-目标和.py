class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        if len(nums) == 0: return 0
        self.result = 0
        self.memo = {}
        # self.backtrack(nums, 0, S)    # Outtime
        self.result = self.dp(nums, 0, S)
        return self.result

    def backtrack(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                self.result += 1
            return
        rest += nums[i]
        self.backtrack(nums, i + 1, rest)
        rest -= nums[i]
        rest -= nums[i]
        self.backtrack(nums, i + 1, rest)
        rest += nums[i]

    def dp(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                return 1
            return 0
        key = str(i) + ',' + str(rest)
        if key in self.memo.keys():
            return self.memo[key]
        result = self.dp(nums, i+1, rest-nums[i]) + self.dp(nums, i+1, rest+nums[i])
        self.memo[key] = result
        return result

if __name__=='__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3   # 5
    solution = Solution()
    result = solution.findTargetSumWays(nums, S)
    print(result)