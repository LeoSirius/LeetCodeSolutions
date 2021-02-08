from typing import *

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = [1] * len(arr)
        down = [1] * len(arr)

        res = 1
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                down[i] = up[i-1] + 1
            elif arr[i-1] < arr[i]:
                up[i] = down[i-1] + 1
            else:
                up[i] = down[i] = 1
            res = max(res, up[i], down[i])

        return res


def test(test_name, arr, expected):
    res = Solution().maxTurbulenceSize(arr)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    arr1 = [9,4,2,10,7,8,8,1,9]
    expected1 = 5
    test('test1', arr1, expected1)

    arr2 = [4,8,12,16]
    expected2 = 2
    test('test2', arr2, expected2)

    arr3 = [100]
    expected3 = 1
    test('test3', arr3, expected3)


# Given an integer array arr, return the length of a maximum size 
# turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between 
# each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of
#  arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
#  

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2

# Example 3:

# Input: arr = [100]
# Output: 1
#  

# Constraints:

# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109

