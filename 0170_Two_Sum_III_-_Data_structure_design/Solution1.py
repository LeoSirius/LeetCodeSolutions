class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        _set = set()
        for n in self.nums:
            n2find = value - n
            if n2find in _set:
                return True
            _set.add(n)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)



def test1():
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    res1 = obj.find(4)
    res2 = obj.find(7)
    if (res1, res2) == (True, False):
        print('test1 success.')
    else:
        print('test1 failed.')


def test2():
    obj = TwoSum()
    obj.add(3)
    obj.add(1)
    obj.add(2)
    res1 = obj.find(3)
    res2 = obj.find(6)
    if (res1, res2) == (True, False):
        print('test2 success.')
    else:
        print('test2 failed.')


def test3():
    obj = TwoSum()
    obj.add(0)
    obj.add(0)
    res1 = obj.find(0)
    if res1 == True:
        print('test3 success.')
    else:
        print('test3 failed.')


if __name__ == '__main__':
    test1()
    test2()
    test3()
