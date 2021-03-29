class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            current_bit = n & 1
            bits.append(current_bit)
            n >>= 1

        res = 0
        base = 1
        bits.reverse()
        for bit in bits:
            res += bit * base
            base *= 2
        return res


def test(test_name, n, expected):
    res = Solution().reverseBits(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 43261596
    expected1 = 964176192
    test("test1", n1, expected1)

    n2 = 4294967293
    expected2 = 3221225471
    test("test2", n2, expected2)

# Reverse bits of a given 32 bits unsigned integer.

# Example 1:

# Input: 00000010100101000001111010011100  # 43261596
# Output: 00111001011110000010100101000000 # 964176192
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2:

# Input: 11111111111111111111111111111101   # 4294967293
# Output: 10111111111111111111111111111111  # 3221225471
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
#  

# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
#  

# Follow up:

# If this function is called many times, how would you optimize it?
