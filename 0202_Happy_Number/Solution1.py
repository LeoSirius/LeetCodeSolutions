class Solution:
    def digit_square_sum(self, n):
        digits = [int(e) for e in str(n)]
        return sum([e * e for e in digits])

    def isHappy(self, n: int) -> bool:
        slow = self.digit_square_sum(n)
        fast = self.digit_square_sum(n)
        fast = self.digit_square_sum(fast)

        while fast != slow:
            slow = self.digit_square_sum(slow)
            fast = self.digit_square_sum(fast)
            fast = self.digit_square_sum(fast)
        return fast == 1


def test(test_name, n, expected):
    res = Solution().isHappy(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 19
    expected1 = True
    test('test1', n1, expected1)
