class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        offset = 0
        while m != n:
            m >>= 1
            n >>= 1
            offset += 1
        return n << offset


def test(test_name, m, n, expected):
    res = Solution().rangeBitwiseAnd(m, n)
    print(res)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    m1, n1 = 5, 7
    expected1 = 4
    test('test1', m1, n1, expected1)

    m2, n2 = 0, 1
    expected2 = 0
    test('test2', m2, n2, expected2)

    m3, n3 = 0, 2147483647
    expected3 = 0
    test('test3', m3, n3, expected3)


# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4

# Example 2:

# Input: [0,1]
# Output: 0

