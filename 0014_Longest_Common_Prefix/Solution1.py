from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = 0

        def check_rows(p):
            for row in range(1, len(strs)):
                if p >= len(strs[row]) or strs[row][p] != strs[row-1][p]:
                    return False
            return True

        while True:
            if p >= len(strs[0]):
                break

            if not check_rows(p):
                break

            p += 1

        return strs[0][:p]


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

    strs2 = ["aca","cba"]
    expected2 = ''
    test('test2', strs2, expected2)
