class Solution:
    """
    传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
    传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
    返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
    """
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)+1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, weights, D, cap):
        i = 0
        len_wights = len(weights)
        for day in range(D):
            lastCap = cap - weights[i]
            while lastCap >= 0:
                i += 1
                if i == len_wights: return True
                lastCap = lastCap - weights[i]
        return False

if __name__=='__main__':
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5                               # 15
    # weights = [3, 2, 2, 4, 1, 4]
    # D = 3                               # 6
    solution = Solution()
    result = solution.shipWithinDays(weights, D)
    print(result)
