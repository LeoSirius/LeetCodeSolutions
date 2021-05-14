class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2

        if n == 1:
            return one
        elif n == 2:
            return two

        for i in range(2, n):
            cur = one + two
            one, two = two, cur
        return cur


def test(test_name, n, expected):
    res = Solution().climbStairs(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 2
    expected1 = 2
    test('test1', n1, expected1)

    n2 = 3
    expected2 = 3
    test('test2', n2, expected2)

    n3 = 1
    expected3 = 1
    test('test3', n3, expected3)
