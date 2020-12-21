class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])

def test(test_name, s, expected):
    res = Solution().lengthOfLastWord(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "Hello World";
    expected1 = 5;
    test("test1", s1, expected1);

    s2 = "Today is a nice day";
    expected2 = 3;
    test("test2", s2, expected2);

    s3 = "a ";
    expected3 = 1;
    test("test3", s3, expected3);
