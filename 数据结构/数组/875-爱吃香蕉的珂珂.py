class Solution:
    """
        珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
        珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，
        她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
        返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
    """
    def minEatingSpeed(self, piles, H) :
        left, right = 1, max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, piles, speed, H):
        time = 0
        for pile in piles:
            if pile % speed > 0:
                time += pile // speed + 1
            else:
                time += pile // speed
        return time <= H

if __name__=='__main__':
    piles = [3, 6, 7, 11]
    H = 8                   # 4
    solution = Solution()
    result = solution.minEatingSpeed(piles, H)
    print(result)
