from typing import *

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            # 走到网格边界外的格子里，边长 + 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            # 走到相邻的水里，边长 + 1
            if grid[r][c] == 0:
                return 1
            
            # 是水，或者是走过的，则跳过
            if grid[r][c] != 1:
                return 0

            grid[r][c] = 2  # 标记走过的为2
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)   # 题目保证了只有一个连通岛
        return 0



def test(test_name, grid, expected):
    res = Solution().islandPerimeter(grid)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    grid1 = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    expected1 = 16
    test('test1', grid1, expected1)

    grid2 = [[1]]
    expected2 = 4
    test('test2', grid2, expected2)

    grid3 = [[1,0]]
    expected3 = 4
    test('test3', grid3, expected3)


# You are given row x col grid representing a map where grid[i][j] = 1 represents 
# land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island
#  (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected 
# to the water around the island. One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
