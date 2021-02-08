class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if not k:
            return 1

        def get_digit_sum(x):
            return sum([int(digit) for digit in str(x)])

        res = 1
        que = [(0,0)]
        move_map = [[0] * n for _ in range(m)]
        move_map[0][0] = 1

        dx, dy = (1, 0), (0, 1)

        while que:
            (x, y) = que.pop(0)
            for i in range(2):
                tx, ty = x + dx[i], y + dy[i]
                if (m <= tx or
                    n <= ty or
                    move_map[tx][ty] or
                    (get_digit_sum(tx) + get_digit_sum(ty) > k)):
                    continue
                move_map[tx][ty] = 1
                que.append((tx, ty))
                res += 1
        return res


def test(test_name, m, n, k, expected):
    res = Solution().movingCount(m, n, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    m1, n1, k1 = 2, 3, 1
    expected1 = 3
    test('test1', m1, n1, k1, expected1)

    m2, n2, k2 = 3, 1, 0
    expected2 = 1
    test('test2', m2, n2, k2, expected2)


# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（
# 不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
# 但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3

# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1

# 提示：
# 1 <= n,m <= 100
# 0 <= k <= 20