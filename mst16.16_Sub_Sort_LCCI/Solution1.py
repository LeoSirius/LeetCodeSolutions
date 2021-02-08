from typing import *

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        l, r = -1, -1
        if not array:
            return [l, r]

        size = len(array)
        _max, _min = -float('inf'), float('inf')

        for i in range(size):
            if array[i] < _max:
                r = i
            else:
                _max = max(_max, array[i])

            if array[size-1-i] > _min:
                l = size-1-i
            else:
                _min = min(_min, array[size-1-i])

        return [l, r]


def test(test_name, array, expected):
    res = Solution().subSort(array)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    array1 = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    expected1 = [3,9]
    test('test1', array1, expected1)


# Given an array of integers, write a method to find indices 
# m and n such that if you sorted elements m through n, 
# the entire array would be sorted. Minimize n - m (that is, 
# find the smallest such sequence).

# Return [m,n]. If there are no such m and n (e.g. the array is
#  already sorted), return [-1, -1].

# Example:

# Input:  [1,2,4,7,10,11,7,12,6,7,16,18,19]
# Output:  [3,9]
# Note:

# 0 <= len(array) <= 1000000

