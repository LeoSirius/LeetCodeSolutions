from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        while l < r:
            water = max(water, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water


def test(test_name, height, expected):
    slt = Solution()
    res = slt.maxArea(height)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    height1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    test('test1', height1, expected1)