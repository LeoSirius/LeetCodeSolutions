from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


def test(test_name, s, expected):
    Solution().reverseString(s)
    if s == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    expected1 = ["o","l","l","e","h"]
    test('test1', s1, expected1)

    s2 = ["H","a","n","n","a","h"]
    expected2 = ["h","a","n","n","a","H"]
    test('test2', s2, expected2)


# Write a function that reverses a string. 
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist 
# of printable ascii characters.

#  

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
