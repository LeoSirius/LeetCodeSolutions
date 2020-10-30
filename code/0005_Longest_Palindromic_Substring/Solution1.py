class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        res = ''

        for l in range(len(s)-1, -1, -1):
            for r in range(l, len(s)):
                dp[l][r] = s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1])
                if dp[l][r] and len(res) < (r - l + 1):
                    res = s[l:r+1]
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

