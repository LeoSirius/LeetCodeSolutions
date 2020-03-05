from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


def test(test_name, height, expected):
    slt = Solution()
    res = slt.maxArea(height)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    height1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    test('test1', height1, expected1)
