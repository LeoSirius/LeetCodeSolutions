from typing import *
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0,0,0)]   # 三元组，分别是：当前的最小effort，x索引，y索引
        dist = [0] + [float('inf')] * (m * n - 1) # 把二维放到一维里
        seen = set()                              # 存放已经确定的点的一维化索引

        while q:
            effort, x, y = heapq.heappop(q)
            next_idx = x * n + y

            if next_idx in seen:
                continue

            if (x, y) == (m-1, y-1):
                break

            seen.add(next_idx)

            for nx, ny in [(x+1, y), (x-1, y), (x,y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n and\
                    max(effort, abs(heights[x][y]-heights[nx][ny])) < dist[nx * n + ny]:
                    dist[nx * n + ny] = max(effort, abs(heights[x][y]-heights[nx][ny]))
                    heapq.heappush(q, (dist[nx * n + ny], nx, ny))

        return dist[m * n - 1]


def test(test_name, heights, expected):
    res = Solution().minimumEffortPath(heights)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    heights1 = [
        [1,2,2],
        [3,8,2],
        [5,3,5]]
    expected1 = 2
    test('test1', heights1, expected1)

    heights2 = [
        [1,2,3],
        [3,8,4],
        [5,3,5]]
    expected2 = 1
    test('test2', heights1, expected1)

    heights3 = [
        [1,2,1,1,1],
        [1,2,1,2,1],
        [1,2,1,2,1],
        [1,2,1,2,1],
        [1,1,1,2,1]]
    expected3 = 0
    test('test3', heights3, expected3)



# You are a hiker preparing for an upcoming hike. 
# You are given heights, a 2D array of size rows x columns, 
# where heights[row][col] represents the height of cell (row, col). 
# You are situated in the top-left cell, (0, 0), and you hope to 
# travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
# You can move up, down, left, or right, and you wish to find a route 
# that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights 
# between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left
#  cell to the bottom-right cell.

#  

# Example 1:



# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference
#  of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum 
# absolute difference is 3.
# Example 2:



# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference 
# of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:


# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
#  

# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

