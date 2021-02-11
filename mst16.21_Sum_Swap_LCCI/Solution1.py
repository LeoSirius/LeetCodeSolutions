from typing import *

class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:

        diff = sum(array1) - sum(array2)

        if diff & 1:
            return []

        diff >>= 1
        s2 = set(array2)
        for n in array1:
            if n - diff in s2:
                return [n, n - diff]

        return []


def test(test_name, array1, array2, expected_arr):
    res = Solution().findSwapValues(array1, array2)
    if res in expected_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    array11 = [4, 1, 2, 1, 1, 2]
    array21 = [3, 6, 3, 3]
    expected_arr1 = [[1,3],[4,6]]
    test('test1', array11, array21, expected_arr1)

    array12 = [1, 2, 3]
    array22 = [4, 5, 6]
    expected_arr2 = [[]]
    test('test2', array12, array22, expected_arr2)


# Given two arrays of integers, find a pair of values 
# (one value from each array) that you can swap to give the
#  two arrays the same sum.

# Return an array, where the first element is the element in 
# the first array that will be swapped, and the second element
#  is another one in the second array. If there are more than one answers,
#   return any one of them. If there is no answer, return an empty array.

# Example:

# Input: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
# Output: [1, 3]
# Example:

# Input: array1 = [1, 2, 3], array2 = [4, 5, 6]
# Output: []
# Note:

# 1 <= array1.length, array2.length <= 100000

