from typing import *

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        # 排除 全升 和 全降 的情况。这两种情况返回False
        if A[0] >= A[1]:
            return False
        if A[-1] >= A[-2]:
            return False

        up = True
        for i in range(1, len(A)):
            if A[i-1] == A[i]:      # 只要有相等的出现，就返回false
                return False

            if up:
                if A[i-1] >= A[i]:
                    up = False
            else:
                if A[i-1] <= A[i]:
                    return False
        return True


def test(test_name, A, expected):
    res = Solution().validMountainArray(A)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    A1 = [2,1]
    expected1 = False
    test('test1', A1, expected1)

    A2 = [3,5,5]
    expected2 = False
    test('test2', A2, expected2)

    A3 = [0,3,2,1]
    expected3 = True
    test('test3', A3, expected3)

    A4 = [1,3,2]
    expected4 = True
    test('test4', A4, expected4)

    A5 = [0,1,2,3,4,5,6,7,8,9]
    expected5 = False
    test('test5', A5, expected5)

    A6 = [9,8,7,6,5,4,3,2,1,0]
    expected6 = False
    test('test6', A6, expected6)

# Given an array A of integers, return true if and only if it is a 
# valid mountain array.

# Recall that A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# Example 1:

# Input: [2,1]
# Output: false
# Example 2:

# Input: [3,5,5]
# Output: false
# Example 3:

# Input: [0,3,2,1]
# Output: true
#  

# Note:

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 

