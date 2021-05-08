from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _len = len(numbers)

        def bi_search(l, r, x):
            while l <= r:
                m = l + (r - l) // 2
                if x > numbers[m]:
                    l = m + 1
                elif x < numbers[m]:
                    r = m - 1
                else:
                    return m
            return -1

        for i, n in enumerate(numbers):
            num2find = target - n
            other_idx = bi_search(i+1, _len-1, num2find)
            if other_idx != -1:
                return [i+1, other_idx + 1]

        return []


def test(test_name, numbers, target, expected):
    res = Solution().twoSum(numbers, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    numbers1 = [2,7,11,15]
    target1 = 9
    expected1 = [1,2]
    test('test1', numbers1, target1, expected1)

    numbers2 = [2,3,4]
    target2 = 6
    expected2 = [1,3]
    test('test2', numbers2, target2, expected2)

    numbers3 = [-1, 0]
    target3 = -1
    expected3 = [1,2]
    test('test3', numbers3, target3, expected3)
