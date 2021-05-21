class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        _len1, _len2 = len(haystack), len(needle)
        if _len2 > _len1:
            return -1

        p1, p2 = 0, 0
        while p1 < _len1 and p2 < _len2:
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 = p1 - p2 + 1    # 从 start 开始 p1 和 p2 走了一样的长度，减去这个长度再+1，即回到 start + 1
                p2 = 0

        if p2 != _len2:
            return -1
        return p1 - _len2


def test(test_name, haystack, needle, expected):
    res = Solution().strStr(haystack, needle)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    haystack1 = "hello";
    needle1 = "ll";
    expected1 = 2;
    test("test1", haystack1, needle1, expected1);

    haystack2 = "aaaaa";
    needle2 = "bba";
    expected2 = -1;
    test("test2", haystack2, needle2, expected2);

    haystack3 = "";
    needle3 = "";
    expected3 = 0;
    test("test3", haystack3, needle3, expected3);

    haystack4 = "aaa"
    needle4 = "aaaa"
    expected4 = -1
    test('test4', haystack4, needle4, expected4)

    haystack5 = "a"
    needle5 = ""
    expected5 = 0
    test("test5", haystack5, needle5, expected5)
