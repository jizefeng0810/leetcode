
class Solution:
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    """
    def canJump(self, nums) -> bool:
        nums_len = len(nums)
        if 0 not in nums or nums_len == 1:
            return True
        farthest = 0
        for i in range(nums_len-1):
            farthest = max(farthest, i+nums[i])
            if farthest <= i: return False
        return True

if __name__=='__main__':
    nums = [2,3,1,1,4]      # 1
    nums = [3,2,1,0,4]      # 0
    nums = [2,0,0]          # 1
    solution = Solution()
    result = solution.canJump(nums)
    print(result)