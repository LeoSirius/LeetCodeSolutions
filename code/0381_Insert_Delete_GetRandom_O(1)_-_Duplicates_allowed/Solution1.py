import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []     # 保存数
        self.idx = {}      # key是数，val是数在nums中的下标集合


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)

        # 把val在nums中的索引放到集合中
        if val not in self.idx:
            self.idx[val] = set()
        self.idx[val].add(len(self.nums)-1)

        return len(self.idx[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.idx or len(self.idx[val]) == 0:
            return False

        # 找出val的一个下标i, 并从集合中移出
        i = self.idx[val].pop()
        size = len(self.nums)

        # 把nums[i]和nums[nums.length-1]交换
        self.nums[i], self.nums[size-1] = self.nums[size-1], self.nums[i]

        # 并把last数在集合中的索引更新,
        # 这里需要先add再remove，比如test2()，前面已经pop过了1的索引，在remove就会报错
        last = self.nums[i]
        self.idx[last].add(i)
        self.idx[last].remove(size-1)

        self.nums.pop()  # 把要remove的元素pop掉
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]




# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def test1():
    obj = RandomizedCollection()
    res1 = obj.insert(1)          # True
    res2 = obj.insert(1)          # False
    res3 = obj.insert(2)          # True
    res4 = obj.getRandom()        # 1 with the probability 2/3, and returns 2 with the probability 1/3.
    res5 = obj.remove(1)          # True
    res6 = obj.getRandom()        # return 1 and 2 both equally likely.

    if res1 == True and res2 == False and res3 == True and res4 in [1,2] and res5 == True and res6 in [1,2]:
        print('test1 success.')
    else:
        print('test1 failed.')

def test2():
    obj = RandomizedCollection()
    res1 = obj.insert(1)   # True
    res2 = obj.remove(1)   # True
    res3 = obj.insert(1)

    if res1 == res2 == res3 == True:
        print('test2 success.')
    else:
        print('test2 failed.')


def test3():
    obj = RandomizedCollection()
    res1 = obj.insert(-1)     # True
    res2 = obj.remove(-2)     # False
    res3 = obj.insert(-2)     # True
    res4 = obj.getRandom()    # [-1, -2]
    res5 = obj.remove(-1)     # True
    res6 = obj.insert(-2)     # False
    res7 = obj.getRandom()    # [-2]

    if (res1 == True and
        res2 == False and
        res3 == True and
        res4 in [-1, -2] and
        res5 == True and
        res6 == False and
        res7 in [-2]):
        print('test3 success.')
    else:
        print('test3 failed.')


# ["RandomizedCollection","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[-1],[-2],[-2],[],[-1],[-2],[]]

if __name__ == "__main__":
    test1()
    test2()
    test3()


# Design a data structure that supports all following 
# operations in average O(1) time.

# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
# Example:

# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();

# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);

# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);

# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);

# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();

# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);

# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
