class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = {}
        _set = set()
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mapper:
                if words[i] in _set:
                    return False
                _set.add(words[i])
                mapper[pattern[i]] = words[i]
            elif mapper[pattern[i]] != words[i]:
                return False

        return True


def test(test_name, pattern, s, expected):
    res = Solution().wordPattern(pattern, s)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == "__main__":
    pattern1, s1 = "abba", "dog cat cat dog"
    expected1 = True
    test('test1', pattern1, s1, expected1)

    pattern2, s2 = "abba", "dog cat cat fish"
    expected2 = False
    test('test2', pattern2, s2, expected2)

    pattern3, s3 = "aaaa", "dog cat cat dog"
    expected3 = False
    test('test3', pattern3, s3, expected3)

    pattern4, s4 = "abba", "dog dog dog dog"
    expected4 = False
    test('test4', pattern4, s4, expected4)


# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Example 4:

# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
#  

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
