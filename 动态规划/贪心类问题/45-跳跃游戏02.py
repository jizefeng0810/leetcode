
class Solution:
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    现在的问题是，保证你一定可以跳到最后一格，请问你最少要跳多少次，才能跳过去。
    """
    def jump(self, nums) -> bool:
        end, farthest = 0, 0
        jumps = 0
        for i in range(len(nums)-1):
            farthest = max(nums[i]+i, farthest)
            if i == end:
                jumps += 1
                end = farthest
        return jumps

if __name__=='__main__':
    nums = [2,3,1,1,4]      # 2
    solution = Solution()
    result = solution.jump(nums)
    print(result)