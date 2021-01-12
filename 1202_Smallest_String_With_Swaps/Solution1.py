from typing import *
import collections

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root = [-1] * len(s)

        def find(x):
            if root[x] == -1:
                return x
            root[x] = find(root[x])
            return root[x]

        def join(a, b):
            A, B = find(a), find(b)
            if A != B:
                root[A] = B

        for a, b in pairs:
            join(a, b)

        # key是根，value是这个连通分量里的所有索引（包括根）
        connect_components = collections.defaultdict(list)
        # 注意这个connect_components的value list必须是递增的，因为后面排序用的是这个
        for i in range(len(s)):
            connect_components[find(i)].append(i)

        res = list(s)
        for nodes in connect_components.values():
            indices = nodes
            string = sorted(res[node] for node in nodes)
            for i, ch in zip(indices, string):
                res[i] = ch

        return ''.join(res)


def test(test_name, s, pairs, expected):
    res = Solution().smallestStringWithSwaps(s, pairs)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "dcab"
    pairs1 = [[0,3],[1,2]]
    expected1 = "bacd"
    test('test1', s1, pairs1, expected1)

    s2 = "dcab"
    pairs2 = [[0,3],[1,2],[0,2]]
    expected2 = "abcd"
    test('test2', s2, pairs2, expected2)

    s3 = "cba"
    pairs3 = [[0,1],[1,2]]
    expected3 = "abc"
    test('test3', s3, pairs3, expected3)


# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 
# pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

# 示例 1:

# 输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"

# 示例 2：

# 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd"

# 示例 3：

# 输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"

# 提示：

# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s 中只含有小写英文字母

