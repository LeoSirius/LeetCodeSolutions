from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        for ch in s1:
            mp[ch] += 1

        l, r = 0, 0
        while r < len(s2):
            ch = s2[r]
            r += 1
            mp[ch] -= 1     # r位置的ch入窗
            while l < r and mp[ch] < 0:
                mp[s2[l]] += 1
                l += 1      # l位置的ch出窗
            
            if r - l == len(s1):
                return True

        return False


def test(test_name, s1, s2, expected):
    res = Solution().checkInclusion(s1, s2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s11 = 'ab'
    s21 = 'eidbaooo'
    expected1 = True
    test('test1', s11, s21, expected1)

    s12 = 'ab'
    s22 = 'eidboaoo'
    expected2 = False
    test('test2', s12, s22, expected2)


# Given two strings s1 and s2, write a function to return true 
# if s2 contains the permutation of s1. In other words, 
# one of the first string's permutations is the substring of 
# the second string.

#  

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#  

# Constraints:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

