import functools
class Solution:
    """
        给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
        这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
    """
    def maxEnvelopes(self, envelopes) -> int:
        def compareRule(a, b):
            if (a[0] == b[0]):
                return b[1] - a[1]
            return a[0] - b[0]

        envelopes.sort(key=functools.cmp_to_key(compareRule))
        height = [0] * len(envelopes)
        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]
        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums):
        piles, n = 0, len(nums)
        top = [0] * n
        for i in range(n):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid + 1
            if left == piles:
                piles += 1
            top[left] = poker
        return piles



if __name__=='__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]   # 3
    solution = Solution()
    result = solution.maxEnvelopes(envelopes)
    print(result)
