class Solution:
    """
        给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
    """
    def intervalIntersection(self, A, B) -> int:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a1, a2 = A[i]
            b1, b2 = B[j]
            if b2 >= a1 and a2 >=b1:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2: j+=1
            else: i+=1
        return res



if __name__=='__main__':
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    solution = Solution()
    result = solution.intervalIntersection(A, B)
    print(result)
