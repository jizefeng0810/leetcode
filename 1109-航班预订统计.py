class Difference:
    def __init__(self): # 差分数组
        self.diff = []
    def Difference(self, nums):
        assert len(nums) > 0
        self.diff = [nums[0]]*len(nums)
        for i in range(1, len(nums)):   # 构造差分数组
            self.diff[i] = nums[i] - nums[i-1]
    def increment(self, i, j, val):     # 给闭区间 [i,j] 增加 val（可以是负数
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val
    def result(self):   # 根据差分数组构造结果数组
        res = []
        res.append(self.diff[0])
        for i in range(1, len(self.diff)):
            res.append(res[-1]+self.diff[i])
        return res

class Solution:
    def corpFlightBookings(self, bookings, n) -> int:
        nums = [0]*n
        df = Difference()
        df.Difference(nums)
        for i, j, val in bookings:
            df.increment(i-1,j-1,val)
        return df.result()

if __name__=='__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5   # [10,55,45,25,25]
    solution = Solution()
    result = solution.corpFlightBookings(bookings, n)
    print(result)
