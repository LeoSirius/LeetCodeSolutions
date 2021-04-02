from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        _sum = sum(height)  # 柱体的所有体积
        l, r = 0, len(height) - 1

        volumn, high = 0, 1
        while l <= r:
            while l <= r and height[l] < high:
                l += 1
            while l <= r and height[r] < high:
                r -= 1
            volumn += r - l + 1
            high += 1
        return volumn - _sum


def test(test_name, height, expected):
    res = Solution().trap(height)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected1 = 6
    test('test1', height1, expected1)

    height2 = [1]
    expected2 = 0
    test('test2', height2, expected2)
