class Solution:
    """
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    请找出所有满足条件且不重复的三元组。
    """
    def threeSum(self, nums):
        n = len(nums)
        if not n or n < 3: return []
        res = []
        nums.sort() # 小到大排序
        for i in range(n):
            if nums[i] > 0:  # 元素i大于0时，三数之和为0不可能成立
                return res
            if i > 0 and nums[i] == nums[i-1]:  # 跳过重复数
                continue
            left, right = i+1, n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:    # 跳过重复数
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 跳过重复数
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

if __name__=='__main__':
    nums = [-1, 0, 1, 2, -1, -4]    # [[-1,-1,2],[-1,0,1]]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)
