from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0] * len(nums)
        self.presum[0] = nums[0]
        for i in range(1, len(nums)):
            self.presum[i] = self.presum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.presum[right] - self.presum[left-1]
        return self.presum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


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

