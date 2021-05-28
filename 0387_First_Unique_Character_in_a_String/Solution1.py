from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


def test(test_name, s, expected):
    res = Solution().firstUniqChar(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'leetcode'
    expected1 = 0
    test('test1', s1, expected1)

    s2 = 'loveleetcode'
    expected2 = 2
    test('test2', s2, expected2)

    s3 = 'aabb'
    expected3 = -1
    test('test3', s3, expected3)
