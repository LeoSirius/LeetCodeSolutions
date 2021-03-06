from typing import *


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stk = []

        for i in range(2 * N):
            while stk and nums[stk[-1]] < nums[i%N]:
                res[stk.pop()] = nums[i%N]
            stk.append(i%N)
        return res


def test(test_name, nums, expected):
    res = Solution().nextGreaterElements(nums)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,1]
    expected1 = [2,-1,2]
    test('test1', nums1, expected1)

