class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # case 1 abcba
            left, right = i, i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                new_str = s[left:right+1]
                if len(new_str) > len(res):
                    res = new_str
                left -= 1
                right += 1
            # case 2 abba
            left, right = i, i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                new_str = s[left:right+1]
                if len(new_str) > len(res):
                    res = new_str
                left -= 1
                right += 1
        return res

def test(test_name, s, expected):
    res = Solution().longestPalindrome(s)
    if res in expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = "babad"
    expected1 = ['bab', 'aba']
    test('tset1', s1, expected1)

    s2 = "cbbd"
    expected2 = ["bb"]
    test('test2', s2, expected2)

    s3 = ''
    expected3 = ['']
    test('test3', s3, expected3)
