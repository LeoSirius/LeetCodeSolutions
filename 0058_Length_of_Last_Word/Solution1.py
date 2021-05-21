class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if res == 0: continue
                else: break
            res += 1
        return res


def test(test_name, s, expected):
    res = Solution().lengthOfLastWord(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "Hello World"
    expected1 = 5
    test("test1", s1, expected1)

    s2 = " "
    expected2 = 0
    test("test2", s2, expected2)

    s3 = "a "
    expected3 = 1
    test("test3", s3, expected3)

    s4 = "Today is a nice day"
    expected4 = 3
    test("test4", s4, expected4)
