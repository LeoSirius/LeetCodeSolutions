from typing import *

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                idx = i
                break
        return idx


def test(test_name, arr, expected):
    res = Solution().peakIndexInMountainArray(arr)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    arr1 = [0,1,0]
    expected1 = 1
    test('test1', arr1, expected1)

    arr2 = [0,2,1,0]
    expected2 = 1
    test('test2', arr2, expected2)

    arr3 = [0,10,5,2]
    expected3 = 1
    test('test3', arr3, expected3)

    arr4 = [3,4,5,1]
    expected4 = 2
    test('test4', arr4, expected4)

    arr5 = [24,69,100,99,79,78,67,36,26,19]
    expected5 = 2
    test('test5', arr5, expected5)
