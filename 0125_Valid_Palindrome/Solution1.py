class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return l == r or l == (r+1)


def test(test_name, s, expected):
    res = Solution().isPalindrome(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama";
    expected1 = True;
    test("test1", s1, expected1);

    s2 = "race a car";
    expected2 = False;
    test("test2", s2, expected2);
