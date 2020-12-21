class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remain = len(num)-k

        for n in num:
            while k and stk and stk[-1] > n:
                stk.pop()
                k -= 1
            stk.append(n)

        return ''.join(stk[:remain]).lstrip('0') or '0'


def test(test_name, num, k, expected):
    res = Solution().removeKdigits(num, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    num1 = "1432219"
    k1 = 3
    expected1 = "1219"
    test('test1', num1, k1, expected1)

    num2 = "10200"
    k2 = 1
    expected2 = "200"
    test('test2', num2, k2, expected2)

    num3 = "10"
    k3 = 2
    expected3 = "0"
    test('test3', num3, k3, expected3)

    num4 = '10'
    k4 = 1
    expected4 = '0'
    test('test4', num4, k4, expected4)


# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.


# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.


# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

