from typing import *

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        s = 0
        res = []
        l, r = 1, 1

        # s是[l,r)的和
        while l <= target // 2:
            if s < target:
                s += r
                r += 1
            elif s > target:
                s -= l
                l += 1
            else:
                res.append([n for n in range(l, r)])
                s -= l
                l += 1

        return res


def test(test_name, target, expected):
    res = Solution().findContinuousSequence(target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    target1 = 9
    expected1 = [[2,3,4],[4,5]]
    test('test1', target1, expected1)

    target2 = 15
    expected2 = [[1,2,3,4,5],[4,5,6],[7,8]]
    test('test2', target2, expected2)


# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


# 示例 1：

# 输入：target = 9
# 输出：[[2,3,4],[4,5]]

# 示例 2：

# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  

# 限制：

# 1 <= target <= 10^5
