from typing import *

class Solution:
    def permutation(self, s: str) -> List[str]:
        ch_list, res = list(s), []

        def dfs(start):
            if start == len(ch_list)-1:
                res.append(''.join(ch_list))
                return

            d_set = set()
            for i in range(start, len(ch_list)):
                if ch_list[i] in d_set:
                    continue
                d_set.add(ch_list[i])
                ch_list[i], ch_list[start] = ch_list[start], ch_list[i]
                dfs(start+1)
                ch_list[i], ch_list[start] = ch_list[start], ch_list[i]
        dfs(0)
        return res


def test(test_name, s, expected):
    res = Solution().permutation(s)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == "__main__":
    s1 = "abc"
    expected1 = ["abc","acb","bac","bca","cab","cba"]
    test('test1', s1, expected1)


# 输入一个字符串，打印出该字符串中字符的所有排列。

# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

# 示例:
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  

# 限制：

# 1 <= s 的长度 <= 8
