from typing import *

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-1, 1, -1):
            if A[i-2]+A[i-1] > A[i]:
                return A[i-2]+A[i-1]+A[i]
        return 0

def test(test_name, A, expected):
    res = Solution().largestPerimeter(A)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    A1 = [2,1,2]
    expected1 = 5
    test('test1', A1, expected1)

    A2 = [1,2,1]
    expected2 = 0
    test('test2', A2, expected2)

    A3 = [3,2,3,4]
    expected3 = 10
    test('test3', A3, expected3)

    A4 = [3,6,2,3]
    expected4 = 8
    test('test4', A4, expected4)



# Given an array A of positive lengths, 
# return the largest perimeter of a triangle with non-zero area, 
# formed from 3 of these lengths.

# If it is impossible to form any triangle of non-zero area, return 0.


# Example 1:

# Input: [2,1,2]
# Output: 5

# Example 2:

# Input: [1,2,1]
# Output: 0

# Example 3:

# Input: [3,2,3,4]
# Output: 10

# Example 4:

# Input: [3,6,2,3]
# Output: 8
#  

# Note:

# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6


