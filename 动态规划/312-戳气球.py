
class Solution:
    """
        现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。
        求所能获得硬币的最大数量。
    """
    def maxCoins(self, intervals) -> int:
        n = len(intervals)
        intervals.insert(0, 1)
        intervals.append(1)
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1,n+2):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+intervals[i]*intervals[k]*intervals[j])
        return dp[0][n+1]

if __name__=='__main__':
    intervals = [3,1,5,8]    # 1
    solution = Solution()
    result = solution.maxCoins(intervals)
    print(result)
