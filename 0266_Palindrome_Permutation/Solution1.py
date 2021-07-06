from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd_cnt = 0
        for k, v in counter.items():
            if v % 2 == 1:
                odd_cnt += 1
            if odd_cnt > 1:
                return False
        return True


def test(test_name, s, expected):
    res = Solution().canPermutePalindrome(s)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    s1 = 'code'
    expected1 = False
    test('test1', s1, expected1)

    s2 = 'aab'
    expected2 = True
    test('test2', s2, expected2)

    s3 = 'carerac'
    expected3 = True
    test('test3', s3, expected3)
