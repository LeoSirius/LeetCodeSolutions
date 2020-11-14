from typing import *


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p = 0
        for n in arr2:
            cur_p = p
            for i in range(p, len(arr1)):
                if arr1[i] == n:
                    arr1[cur_p], arr1[i] = arr1[i], arr1[cur_p]
                    cur_p += 1
            p = cur_p
        arr1 = arr1[:p] + sorted(arr1[p:])  # arr2中没有的arr1原元素需要是升序
        return arr1


def test(test_name, arr1, arr2, expected):
    res = Solution().relativeSortArray(arr1, arr2)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    arr11 = [2,3,1,3,2,4,6,7,9,2,19]
    arr21 = [2,1,4,3,9,6]
    expected1 = [2,2,2,1,4,3,3,9,6,7,19]
    test('test1', arr11, arr21, expected1)

    arr21 = [28,6,22,8,44,17]
    arr22 = [22,28,8,6]
    expected2 = [22,28,8,6,17,44]
    test('test2', arr21, arr22, expected2)


# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items 
# in arr1 are the same as in arr2.  Elements that don't appear in 
# arr2 should be placed at the end of arr1 in ascending order.

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#  

# Constraints:

# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.

