import random
class RandomizedSet:
    """
        设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valToIndex.keys():
            return False
        self.valToIndex[val] = len(self.num)
        self.num.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valToIndex.keys():
            return False
        index = self.valToIndex[val]
        self.valToIndex[self.num[-1]] = index
        self.num[index] = self.num[-1]
        self.num.pop()
        self.valToIndex.pop(val)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.num[int(random.random() * len(self.num))]


if __name__=='__main__':
    randomSet = RandomizedSet()
    print(randomSet.num)
    print(randomSet.insert(1))
    print(randomSet.num)
    print(randomSet.remove(2))
    print(randomSet.num)
    print(randomSet.insert(2))
    print(randomSet.num)

    print(randomSet.getRandom())

    print(randomSet.remove(1))
    print(randomSet.num)
    print(randomSet.insert(2))
    print(randomSet.num)

    print(randomSet.getRandom())
