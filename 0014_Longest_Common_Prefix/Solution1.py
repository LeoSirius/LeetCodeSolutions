from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res
        min_len = min([len(str) for str in strs])
        for col in range(min_len):
            cur_char = strs[0][col]
            for str in strs:
                if len(str) <= col or str[col] != cur_char:
                    return res
            res += cur_char
        return res


def test(test_name, strs, expected):
    res = Solution().longestCommonPrefix(strs)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    expected1 = 'fl'
    test('test1', strs1, expected1)

    strs2 = []
    expected2 = ''
    test('test2', strs2, expected2)

    strs3 = ["aca","cba"]
    expected3 = ''
    test('test3', strs3, expected3)
