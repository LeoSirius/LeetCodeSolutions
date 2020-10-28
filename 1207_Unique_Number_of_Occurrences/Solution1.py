from typing import *
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dd = defaultdict(int)
        for n in arr:
            dd[n] += 1
        times = set(dd.values())
        return len(times) == len(dd)


def test(test_name, arr, expected):
    res = Solution().uniqueOccurrences(arr)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    arr1 = [1,2,2,1,1,3]
    expected1 = True
    test('test1', arr1, expected1)

    arr2 = [1,2]
    expected2 = False
    test('test2', arr2, expected2)

    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    expected3 = True
    test('test3', arr3, expected3)


# Given an array of integers arr, write a function that returns
# true if and only if the number of occurrences of each value in the
# array is unique.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
# No two values have the same number of occurrences.

# Example 2:

# Input: arr = [1,2]
# Output: false

# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#  

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

