class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ((n & (n-1)) == 0)

def test(test_name, n, expected):
    res = Solution().isPowerOfTwo(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1, expected1 = 1, True
    test('test1', n1, expected1)

    n2, expected2 = 16, True
    test('test2', n2, expected2)

    n3, expected3 = 218, False
    test('test3', n3, expected3)

    n4, expected4 = 0, False
    test('test4', n4, expected4)

# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1

# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16

# Example 3:

# Input: 218
# Output: false

