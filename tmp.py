class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        # if len(haystack) < len(needle):
        #     return -1

        i, p, j = 0, 0, 0
        while i < len(haystack):
            p = i
            j = 0
            while p < len(haystack) and j < len(needle) and haystack[p] == needle[j]:
                p += 1
                j += 1
            if j == len(needle):
                return i
            i += 1
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
