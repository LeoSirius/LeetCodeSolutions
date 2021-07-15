from typing import *


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] > 1:
            arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]


def test(test_name, arr, expected):
    res = Solution().maximumElementAfterDecrementingAndRearranging(arr)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    arr1 = [2,2,1,2,1]
    expected1 = 2
    test('test1', arr1, expected1)

    arr2 = [100,1,1000]
    expected2 = 3
    test('test2', arr2, expected2)

    arr3 = [1,2,3,4,5]
    expected3 = 5
    test('test3', arr3, expected3)
