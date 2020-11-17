import functools
class Solution:
    """
        给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
    """
    def removeCoveredIntervals(self, intervals) -> int:
        def compareRule(a, b):
            if (a[0] == b[0]):
                return b[1] - a[1]
            return a[0] - b[0]

        intervals.sort(key=functools.cmp_to_key(compareRule))
        res = 0
        left, right = intervals[0]
        for i_left, i_right in intervals[1:]:
            if left <= i_left and right >= i_right:
                res+=1
            elif right >= i_left and right <= i_right:
                right = i_right
            elif right < i_left:
                left, right = i_left, i_right
        return len(intervals) - res



if __name__=='__main__':
    intervals = [[1,4],[3,6],[2,8]] # 2
    intervals = [[1,4],[2,3]] # 1
    solution = Solution()
    result = solution.removeCoveredIntervals(intervals)
    print(result)
