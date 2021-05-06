from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _len = len(digits)
        carry = 1
        for i in range(_len - 1, -1, -1):
            n = digits[i] + carry
            digits[i] = n % 10
            carry = n // 10
            if carry == 0:
                break

        if carry:
            digits.insert(0, carry)

        return digits



def test(test_name, digits, expected):
    res = Solution().plusOne(digits)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    digits1 = [1,2,3]
    expected1 = [1,2,4]
    test('test1', digits1, expected1)

    digits2 = [4,3,2,1]
    expected2 = [4,3,2,2]
    test('test2', digits2, expected2)

    digits3 = [0]
    expected3 = [1]
    test('test3', digits3, expected3)

    digits4 = [9, 9]
    expected4 = [1, 0, 0]
    test('test4', digits4, expected4)


# Given a non-empty array of decimal digits representing a non-negative 
# integer, increment one to the integer.

# The digits are stored such that the most significant digit is 
# at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, 
# except the number 0 itself.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:

# Input: digits = [0]
# Output: [1]
#  

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9

