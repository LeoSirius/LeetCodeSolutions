from typing import *


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        dp_row = [0] * len(grid[0])

        for i in range(len(grid)):
            dp_row[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                dp_row[j] = max(dp_row[j-1], dp_row[j]) + grid[i][j]

        return dp_row[-1]


def test(test_name, grid, expected):
    res = Solution().maxValue(grid)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    grid1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    expected1 = 12
    test('test1', grid1, expected1)

    grid2 = [
        [1,2],
        [5,6],
        [1,1]
    ]
    expected2 = 13
    test('test2', grid2, expected2)


