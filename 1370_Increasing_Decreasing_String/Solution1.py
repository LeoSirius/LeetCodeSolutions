class Solution:
    def sortString(self, s: str) -> str:
        bucket = [0] * 26
        for ch in s:
            bucket[ord(ch)-ord('a')] += 1
        
        res = ''
        while len(res) < len(s):
            for i in range(26):
                if bucket[i]:
                    res += chr(ord('a') + i)
                    bucket[i] -= 1
            for i in range(25, -1, -1):
                if bucket[i]:
                    res += chr(ord('a') + i)
                    bucket[i] -= 1
        return res


def test(test_name, s, expected):
    res = Solution().sortString(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "aaaabbbbcccc"
    expected1 = "abccbaabccba"
    test('test1', s1, expected1)

    s2 = "rat"
    expected2 = "art"
    test('test2', s2, expected2)

    s3 = "leetcode"
    expected3 = "cdelotee"
    test('test3', s3, expected3)

    s4 = "ggggggg"
    expected4 = "ggggggg"
    test('test4', s4, expected4)

    s5 = "spo"
    expected5 = "ops"
    test('test5', s5, expected5)


# Given a string s. You should re-order the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

#  

# Example 1:

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

# Example 2:

# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

# Example 3:

# Input: s = "leetcode"
# Output: "cdelotee"

# Example 4:

# Input: s = "ggggggg"
# Output: "ggggggg"

# Example 5:

# Input: s = "spo"
# Output: "ops"
#  

# Constraints:

# 1 <= s.length <= 500
# s contains only lower-case English letters.

