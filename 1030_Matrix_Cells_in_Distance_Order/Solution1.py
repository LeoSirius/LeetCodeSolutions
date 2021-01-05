from typing import *

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        i, j = r0, c0
        que = [[i, j]]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        mp = [[False] * C for _ in range(R)]
        mp[i][j] = True

        while que:
            cur_level_size = len(que)
            while cur_level_size:
                cur_level_size -= 1
                cur_node = que.pop(0)
                res.append(cur_node)

                for i in range(4):
                    x, y = cur_node[0] + dx[i], cur_node[1] + dy[i]
                    if x < 0 or y < 0 or x >= R or y >= C:
                        continue
                    if mp[x][y]:
                        continue
                    que.append([x,y])
                    mp[x][y] = True
        return res


def test(test_name, R, C, r0, c0, expected_arr):
    res = Solution().allCellsDistOrder(R, C, r0, c0)
    if res in expected_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    R1, C1 = 1, 2
    r01, c01 = 0, 0
    expected_arr1 = [
        [[0,0],[0,1]],
    ]
    test('test1', R1, C1, r01, c01, expected_arr1)

    R2, C2 = 2, 2
    r02, c02 = 0, 1
    expected_arr2 = [
        [[0,1],[0,0],[1,1],[1,0]],
        [[0,1],[1,1],[0,0],[1,0]]
    ]
    test('test2', R2, C2, r02, c02, expected_arr2)

    # [
    #     [(0,0), (0,1), (0,2)],
    #     [(1,0), (1,1), (1,2)]
    # ]
    R3, C3 = 2, 3
    r03, c03 = 1, 2
    expected_arr3 = [
        [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]],
        [[1,2],[0,2],[1,1],[1,0],[0,1],[0,0]],
        [[1,2],[1,1],[0,2],[0,1],[1,0],[0,0]],
        [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]],
    ]
    test('test3', R3, C3, r03, c03, expected_arr3)


# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，
# 两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
# （你可以按任何满足此条件的顺序返回答案。）

# 示例 1：

# 输入：R = 1, C = 2, r0 = 0, c0 = 0
# 输出：[[0,0],[0,1]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]


# 示例 2：

# 输入：R = 2, C = 2, r0 = 0, c0 = 1
# 输出：[[0,1],[0,0],[1,1],[1,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
# [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。


# 示例 3：

# 输入：R = 2, C = 3, r0 = 1, c0 = 2
# 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
#  

# 提示：

# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
