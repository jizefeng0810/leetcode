import functools
class Solution:
    """
        给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
        1、先找到最小互不重叠数；
        2、len(n) - 1的结果
    """
    def eraseOverlapIntervals(self, intervals) -> int:
        def compareRule(a, b):
            if a[1] == b[1]: return b[0] - a[0]
            return b[1] - a[1]
        intervals.sort(key=functools.cmp_to_key(compareRule), reverse=True)
        # print(intervals)

        if not intervals: return 0

        end = intervals[0][1]
        result = len(intervals) - 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                result -= 1
                end = intervals[i][1]
        return result

if __name__=='__main__':
    intervals = [[1,2], [2,3], [3,4], [1,3]]    # 1
    # intervals = [ [1,2], [1,2], [1,2] ]         # 2
    # intervals = [ [1,2], [2,3] ]                # 0
    # intervals = []
    solution = Solution()
    result = solution.eraseOverlapIntervals(intervals)
    print(result)
