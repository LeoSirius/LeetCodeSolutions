from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return

        self.presum = [nums[0]]
        for n in nums[1:]:
            self.presum.append(n + self.presum[-1])

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.presum[j]

        return self.presum[j] - self.presum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


def test1():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    res1 = obj.sumRange(0, 2)
    res2 = obj.sumRange(2, 5)
    res3 = obj.sumRange(0, 5)

    if (res1, res2, res3) == (1, -1, -3):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == '__main__':
    test1()

