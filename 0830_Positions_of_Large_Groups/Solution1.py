from typing import *

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        begin, end = 0, 0
        res = []

        if len(s) < 3:
            return res

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                end += 1
            else:
                if end + 1 - begin >= 3:
                    res.append([begin, end])
                begin = i
                end = i

            # 处理一种特殊情况
            if i == len(s) - 1 and end + 1 - begin >= 3:
                res.append([begin, end])

        return res

def test(test_name, s, expected):
    res = Solution().largeGroupPositions(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "abbxxxxzzy"
    expected1 = [[3,6]]
    test('test1', s1, expected1)

    s2 = 'abc'
    expected2 = []
    test('test2', s2, expected2)

    s3 = 'abcdddeeeeaabbbcd'
    expected3 = [[3,5],[6,9],[12,14]]
    test('test3', s3, expected3)

    s4 = "aba"
    expected4 = []
    test('test4', s4, expected4)

    s5 = 'aaa'
    expected5 = [[0, 2]]
    test('test5', s5, expected5)


# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。
# 上例中的 "xxxx" 分组用区间表示为 [3,6] 。

# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。


# 示例 1：

# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。

# 示例 2：

# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。

# 示例 3：

# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb"

# 示例 4：

# 输入：s = "aba"
# 输出：[]
#  
# 提示：

# 1 <= s.length <= 1000
# s 仅含小写英文字母
