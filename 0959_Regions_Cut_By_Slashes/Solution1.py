from typing import *

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        root = [-1 for _ in range(n * n * 4)]

        def find(x):
            if root[x] == -1:
                return x
            root[x] = find(root[x])
            return root[x]

        def merge(a, b):
            A, B = find(a), find(b)
            if A != B:
                root[A] = B

        for i in range(n):
            for j in range(n):
                # idx就是每个square的索引
                # idx * 4 就是每个square里第一个三角形的索引
                idx = i * n + j

                # 对于非最后一行的square，idx + n就是正对着下面那个square
                # 这里把当前square的2号三角形和下面square的0号三角形merge
                if i < n - 1:
                    bottom = idx + n
                    merge(idx * 4 + 2, bottom * 4)

                # 对于非最后一列的square，idx + 1就是正对着右边的那个square
                # 这里把当前square的1号三角形和右边square的3号三角形merge
                if j < n - 1:
                    right = idx + 1
                    merge(idx * 4 + 1, right * 4 + 3)

                # 上边两种处理的是square之间的情况
                # 下面三种是一个square内部的情况
                if grid[i][j] == '/':
                    merge(idx * 4, idx * 4 + 3)
                    merge(idx * 4 + 1, idx * 4 + 2)
                elif grid[i][j] == '\\':
                    merge(idx * 4, idx * 4 + 1)
                    merge(idx * 4 + 2, idx * 4 + 3)
                else:
                    merge(idx * 4, idx * 4 + 1)
                    merge(idx * 4 + 1, idx * 4 + 2)
                    merge(idx * 4 + 2, idx * 4 + 3)

        cnt = 0
        for i in range(n * n * 4):
            if root[i] == -1:
                cnt += 1

        return cnt


def test(test_name, grid, expected):
    res = Solution().regionsBySlashes(grid)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    grid1 = [
        " /",
        "/ "
    ]
    expected1 = 2
    test('test1', grid1, expected1)

    grid2 = [
        " /",
        "  "
    ]
    expected2 = 1
    test('test2', grid2, expected2)

    grid3 = [
        "\\/",   # 注意\\转义后是\
        "/\\"
    ]
    expected3 = 4
    test('test3', grid3, expected3)

    grid4 = [
        "/\\",
        "\\/"
    ]
    expected4 = 5
    test('test4', grid4, expected4)

    grid5 = [
        "//",
        "/ "
    ]
    expected5 = 3
    test('test5', grid5, expected5)



# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square 
# consists of a /, \, or blank space.  These characters divide the 
# square into contiguous regions.

# (Note that backslash characters are escaped, so a \ is represented as "\\".)

# Return the number of regions.


# Example 1:

# Input:
# [
#   " /",
#   "/ "
# ]
# Output: 2

# Input:
# [
#   " /",
#   "  "
# ]
# Output: 1


# Example 3:

# Input:
# [
#   "\\/",
#   "/\\"
# ]
# Output: 4

# Example 4:

# Input:
# [
#   "/\\",
#   "\\/"
# ]
# Output: 5

# Example 5:

# Input:
# [
#   "//",
#   "/ "
# ]
# Output: 3

