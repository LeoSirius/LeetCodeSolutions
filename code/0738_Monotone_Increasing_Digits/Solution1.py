class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = [int(ch) for ch in str(N)]
        i = len(digits)-1

        while i > 0:
            if digits[i-1] > digits[i]:
                digits[i-1] -= 1
                for j in range(i, len(digits)): digits[j] = 9
            i -= 1

        return int(''.join([str(n) for n in digits]))


def test(test_name, N, expected):
    res = Solution().monotoneIncreasingDigits(N)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    N1 = 10
    expected1 = 9
    test('test1', N1, expected1)

    N2 = 1234
    expected2 = 1234
    test('test2', N2, expected2)

    N3 = 332
    expected3 = 299
    test('test3', N3, expected3)

    N4 = 100
    expected4 = 99
    test('test4', N4, expected4)


# Given a non-negative integer N, find the largest number that is
#  less than or equal to N with monotone increasing digits.

# (Recall that an integer has monotone increasing digits if and 
# only if each pair of adjacent digits x and y satisfy x <= y.)

# Example 1:
# Input: N = 10
# Output: 9

# Example 2:
# Input: N = 1234
# Output: 1234

# Example 3:
# Input: N = 332
# Output: 299

# Note: N is an integer in the range [0, 10^9].
