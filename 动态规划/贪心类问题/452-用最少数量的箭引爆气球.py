import functools
class Solution:
    def findMinArrowShots(self, points) -> int:
        def compareRule(a, b):
            if a[1] == b[1]: return b[0] - a[0]
            return b[1] - a[1]
        points.sort(key=functools.cmp_to_key(compareRule), reverse=True)
        print(points)

        if not points: return 0
        end = points[0][1]
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                result += 1
                end = points[i][1]
        return result

if __name__=='__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]       # 2
    points = [[1,2],[3,4],[5,6],[7,8]]          # 4
    solution = Solution()
    result = solution.findMinArrowShots(points)
    print(result)