
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = []
        for i in range(len(s)):
            diffs.append(abs(ord(s[i]) - ord(t[i])))

        l, r = 0, 0
        window_sum = 0
        res = 0

        for r in range(len(s)):
            # 右边不断扩张，逼近maxCost
            window_sum += diffs[r]

            # 右边超过，则左边收缩
            while window_sum > maxCost:
                window_sum -= diffs[l]
                l += 1

            # 更新最大距离
            res = max(res, r - l + 1)

        return res


def test(test_name, s, t, maxCost, expected):
    res = Solution().equalSubstring(s, t, maxCost)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'abcd'
    t1 = 'bcdf'
    maxCost1 = 3
    expected1 = 3
    test('test1', s1, t1, maxCost1, expected1)

    s2 = "abcd"
    t2 = "cdef"
    maxCost2 = 3
    expected2 = 1
    test('test2', s2, t2, maxCost2, expected2)

    s3 = "abcd"
    t3 = "acde"
    maxCost3 = 0
    expected3 = 1
    test('test3', s3, t3, maxCost3, expected3)


# You are given two strings s and t of the same length.
#  You want to change s to t. Changing the i-th character 
#  of s to i-th character of t costs |s[i] - t[i]| that is, 
#  the absolute difference between the ASCII values of the characters.

# You are also given an integer maxCost.

# Return the maximum length of a substring of s that can be changed 
# to be the same as the corresponding substring of t with a cost less
#  than or equal to maxCost.

# If there is no substring from s that can be changed to its corresponding 
# substring from t, return 0.

#  

# Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

# Example 2:

# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.

# Example 3:

# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You can't make any change, so the maximum length is 1.
#  

# Constraints:

# 1 <= s.length, t.length <= 10^5
# 0 <= maxCost <= 10^6
# s and t only contain lower case English letters.
