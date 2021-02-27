from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        for ch in set(s):
            # for every unique char in s
            # if count of that char < k, meanse that char can not appear in subarray, so split by that char
            if s.count(ch) < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))

        # every char's count is >= k, s itself satisfy, return it's length
        return len(s)


def test(test_name, s, k, expected):
    res = Solution().longestSubstring(s, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'aaabb'
    k1 = 3
    expected1 = 3
    test('test1', s1, k1, expected1)

    s2 = 'ababbc'
    k2 = 2
    expected2 = 5
    test('tset2', s2, k2, expected2)

