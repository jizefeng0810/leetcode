class Solution:
    """
        给你一个区间列表，合并所有重叠的区间。
    """
    def merge(self, intervals) -> int:
        intervals.sort()
        res = []
        left, right = intervals[0]
        for i_left, i_right in intervals[1:]:
            if right >= i_left:
                if right <= i_right:
                    right = i_right
            else:
                res.append([left, right])
                left, right = i_left, i_right
        res.append([left, right])
        return res



if __name__=='__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]] # [[1,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]] # [[1,5]]
    # intervals = [[1, 4], [2, 3]]  # [[1,4]]
    solution = Solution()
    result = solution.merge(intervals)
    print(result)
