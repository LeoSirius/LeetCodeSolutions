from typing import *


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        _len = len(nums)

        for k in range(30):
            s1, s2 = 0, 0
            for row in range(_len):
                # print(f'(nums[row] >> k) & 1 = {(nums[row] >> k) & 1}')
                if (nums[row] >> k) & 1:
                    s1 += 1
                else:
                    s2 += 1
            # print(f's1 = {s1}, s2 = {s2}')
            res += s1 * s2
        # print(f'res = {res}')
        return res


def test(test_name, nums, expected):
    res = Solution().totalHammingDistance(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [4,14,2]
    expected1 = 6
    test('test1', nums1, expected1)

    nums2 = [4,14,4]
    expected2 = 4
    test('test2', nums2, expected2)
