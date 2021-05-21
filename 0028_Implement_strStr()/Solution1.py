class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        # 如len(haystack) = 5, len(needle) = 3
        # len(haystack) - len(needle) + 1 = 3
        # i刚好从0到2，i=2时，加上needle的长度，就是haystack的长度
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


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
