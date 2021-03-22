class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res += n & 1
            n >>= 1
        return res


def test(test_name, n, expected):
    res = Solution().hammingWeight(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = int('00000000000000000000000000001011', 2)
    expected1 = 3
    test('test1', n1, expected1)

    n2 = int('00000000000000000000000010000000', 2)
    expected2 = 1
    test('test2', n2, expected2)

    n3 = int('11111111111111111111111111111101', 2)
    expected3 = 31
    test("test3", n3, expected3)


# Write a function that takes an unsigned integer and return 
# the number of '1' bits it has (also known as the Hamming weight).


# Example 1:

# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#  

# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
#  

# Follow up:

# If this function is called many times, how would you optimize it?

