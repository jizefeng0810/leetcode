class Solution:
    """
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中
    是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    """
    def fourSum(self, nums, target):
        n = len(nums)
        if not n or n < 4: return []
        res = []
        nums.sort() # 小到大排序
        for j in range(n):
            if j > 0 and nums[j] == nums[j - 1]:  # 跳过重复数
                continue
            for i in range(j+1, n):
                if i > j+1 and nums[i] == nums[i - 1]:  # 跳过重复数
                    continue
                left, right = i+1, n-1
                while left < right:
                    if nums[j] + nums[i] + nums[left] + nums[right] == target:
                        res.append([nums[j], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:    # 跳过重复数
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:  # 跳过重复数
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[j] + nums[i] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return res

if __name__=='__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    """
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
    """
    # nums = [0, 0, 0, 0]
    # target = 0  # [[0,0,0,0]]
    # nums = [-1,0,1,2,-1,-4]
    # target = -1 # [[-4,0,1,2],[-1,-1,0,1]]
    solution = Solution()
    result = solution.fourSum(nums, target)
    print(result)
