from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(), set()
        for n in nums1:
            s1.add(n)
        for n in nums2:
            s2.add(n)
        return list(s1.intersection(s2))


def test(test_name, nums1, nums2, expected):
    res = Solution().intersection(nums1, nums2)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums11 = [1,2,2,1]
    nums21 = [2,2]
    expected1 = [2]
    test('test1', nums11, nums21, expected1)

    nums12 = [4,9,5]
    nums22 = [9,4,9,8,4]
    expected2 = [9,4]
    test('test2', nums12, nums22, expected2)
