
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct = defaultdict(int)
        for i in range(len(s)):
            dct[s[i]] += 1
            dct[t[i]] -= 1
        for v in dct.values():
            if v != 0:
                return False
        return True


def test(test_name, s, t, expected):
    res = Solution().isAnagram(s, t)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1, t1 = 'anagram', 'nagaram'
    expected1 = True
    test('test1', s1, t1, expected1)

    s2, t2 = 'rat', 'car'
    expected2 = False
    test('test2', s2, t2, expected2)

    s3, t3 = 'ab', 'a'
    expected3 = False
    test('test3', s3, t3, expected3)


# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
