class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i in range(len(s) - 1):
            if mapping[s[i]] >= mapping[s[i+1]]:
                res += mapping[s[i]]
            else:
                res -= mapping[s[i]]
        return res + mapping[s[-1]]