import time

def fib(n):
    """
    时间复杂度 O(2^n)
    :param n: number
    :return: fib value
    """
    if n == 2 or n == 1: return 1
    return fib(n-1) + fib(n-2)

def fib_memory_optimize(memo, n):
    """
    开辟内存存储每个计算过的值
    :param memo:array
    :param n:number
    :return: fib value
    """
    if n == 2 or n == 1: return 1
    if memo[n] != 0: return memo[n]
    memo[n] = fib_memory_optimize(memo, n-1) + fib_memory_optimize(memo, n-2)
    return memo[n]

def fib_dp_optimize(n):
    """
    动态规划求解，从底往上。继续优化方向，dp数组只需要2个变量代替前两个状态
    :param n: number
    :return: fib value
    """
    dp = [0]*n
    dp[0] = dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

if __name__ == '__main__':
    n = 32
    starttime = time.time()
    print(fib(n))
    endtime = time.time()
    print('baoli:', endtime - starttime)

    memo = [0] * (n+1)
    starttime = time.time()
    print(fib_memory_optimize(memo, n))
    endtime = time.time()
    print('memory:', endtime - starttime)

    starttime = time.time()
    print(fib_dp_optimize(n))
    endtime = time.time()
    print('dp:', endtime - starttime)
