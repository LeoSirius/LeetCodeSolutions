from typing import *


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldr, oldc = len(nums), len(nums[0])
        if oldr * oldc != r * c:
            return nums

        res = []
        i, j = 0, 0
        for _ in range(r):
            row = []
            for _ in range(c):
                cur = nums[i][j]
                row.append(cur)
                j += 1
                if j == oldc:
                    i += 1
                    j = 0

            res.append(row)
            if i == oldr:
                break

        return res


def test(test_name, nums, r, c, expected):
    res = Solution().matrixReshape(nums, r, c)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [
        [1,2],
        [3,4],
    ]
    r1, c1 = 1, 4
    expected1 = [[1,2,3,4]]
    test('test1', nums1, r1, c1, expected1)

    nums2 = [
        [1,2],
        [3,4],
    ]
    r2, c2 = 2, 4
    expected2 = [
        [1,2],
        [3,4],
    ]
    test('test2', nums2, r2, c2, expected2)
