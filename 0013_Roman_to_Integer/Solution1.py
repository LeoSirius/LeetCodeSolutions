class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        res = 0
        for i in range(len(s) - 1):
            if mp[s[i]] < mp[s[i + 1]]:
                res -= mp[s[i]]
            else:
                res += mp[s[i]]
        return res + mp[s[-1]]

def test(test_name, s, expected):
    res = Solution().romanToInt(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    test("test1", "MCMXCIV", 1994)
