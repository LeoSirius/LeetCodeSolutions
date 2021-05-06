from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, i = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                n = nums1[p1]
                p1 -= 1
            else:
                n = nums2[p2]
                p2 -= 1
            nums1[i] = n
            i -= 1

        while p1 >= 0:
            nums1[i] = nums1[p1]
            p1 -= 1
            i -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1


def test(test_name, nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    print(f'nums1 = {nums1}')
    if nums1 == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums11 = [1,2,3,0,0,0]
    m1 = 3
    nums21 = [2,5,6]
    n1 = 3
    expected1 = [1,2,2,3,5,6]
    test('test1', nums11, m1, nums21, n1, expected1)

    nums12 = [1]
    m2 = 1
    nums22 = []
    n2 = 0
    expected2 = [1]
    test('test2', nums12, m2, nums22, n2, expected2)

    nums13 = [0]
    m3 = 0
    nums23 = [1]
    n3 = 1
    expected3 = [1]
    test('test3', nums13, m3, nums23, n3, expected3)
