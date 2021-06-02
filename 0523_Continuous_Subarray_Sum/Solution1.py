from typing import *

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = [0] * (len(nums) + 1)
        presum[1] = nums[0]
        for i in range(1, len(nums)+1):
            presum[i] = presum[i-1] + nums[i-1]

        _set = set()
        # 子数组长度至少为 2，所以从 2 开始
        # presum 其实从 1 开始，[0, 2] 刚好就是前两个元素
        for i in range(2, len(nums)+1):
            _set.add(presum[i-2] % k)  # presum[0] = 0 刚好把整除的情况算进去了
            if presum[i] % k in _set:
                return True

        return False


def test(test_name, nums, k, expected):
    res = Solution().checkSubarraySum(nums, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [23,2,4,6,7]
    k1 = 6
    expected1 = True
    test('test1', nums1, k1, expected1)

    nums2 = [23,2,6,4,7]
    k2 = 6
    expected2 = True
    test('test2', nums2, k2, expected2)

    nums3 = [23,2,6,4,7]
    k3 = 13
    expected3 = False
    test('test3', nums3, k3, expected3)

    nums4 = [23,2,4,6,6]
    k4 = 7
    expected4 = True
    test('test4', nums4, k4, expected4)

    nums5 = [0, 0]
    k5 = 1
    expected5 = True
    test('test5', nums5, k5, expected5)
