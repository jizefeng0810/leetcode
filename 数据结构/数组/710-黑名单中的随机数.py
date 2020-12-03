from random import random
class Solution:
    """
        给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。
        对它进行优化使其尽量少调用系统方法 Math.random() 。
        思路：
            定义一个字典,并按照关键字划分为两个区间 [0, N-len(blacklist)], (N-len(blacklist), N)
            然后把左边的区间里面的黑名单元素替换成右边区间白名单元素。
    """
    def __init__(self, N, blacklist):
        self.map = {}
        self.sz = N - len(blacklist)
        for b in blacklist:
            self.map[b] = 666
        last = N -1
        for b in blacklist:
            if b >= self.sz: continue
            while last in self.map.keys():  # (N-len(blacklist), N)没在字典里的即为白名单
                last -= 1
            self.map[b] = last
            last -= 1

    def pick(self) :
        index = int(random() * self.sz)
        if index in self.map.keys():
            return self.map[index]
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

if __name__ == '__main__':
    solution = Solution()
