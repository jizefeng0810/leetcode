class Solution:
    """
        superEggDrop_01：超时
        superEggDrop_02：二分搜索
    """
    def superEggDrop_01(self, K, N):
        memo = {}
        def dp(K,N):
            if K==1: return N
            if N==0:return 0
            if (K,N) in memo:
                return memo[(K,N)]
            res = float('inf')
            for i in range(1,N+1):
                res = min(res, max(dp(K, N-i), dp(K-1, i-1)) + 1)
            memo[(K,N)] = res
            return res
        return dp(K,N)

    def superEggDrop_02(self, K, N):
        memo = {}
        def dp(K,N):
            if K==1: return N
            if N==0:return 0
            if (K,N) in memo:
                return memo[(K,N)]
            res = float('inf')
            # 用二分搜索代替线性搜索
            l,h = 1, N
            while l <= h:
                mid = (l + h) // 2
                broken = dp(K-1, mid - 1)   # 碎
                not_broken = dp(K, N - mid) # 没碎
                # res = min(res, max(碎，没碎) + 1)
                if broken > not_broken:
                    h = mid - 1
                    res = min(res, broken + 1)
                else:
                    l = mid +1
                    res = min(res, not_broken + 1)
            memo[(K,N)] = res
            return res
        return dp(K,N)

if __name__=='__main__':
    K, N = 1, 2     # 2
    K, N = 2, 6     # 3
    K, N = 3, 14    # 4
    K, N = 4, 2000
    import time
    solution = Solution()
    # begin = time.time()
    # result = solution.superEggDrop_01(K, N)
    # end = time.time()
    # print(result)
    # print('Cost time:', end-begin)
    begin = time.time()
    result = solution.superEggDrop_02(K, N)
    end = time.time()
    print(result)
    print('Cost time:', end - begin)