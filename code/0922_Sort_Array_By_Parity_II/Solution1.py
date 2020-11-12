from typing import *

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i = 0
        for n in A:
            if n % 2 == 0:
                res[i] = n
                i += 2
        i = 1
        for n in A:
            if n % 2 == 1:
                res[i] = n
                i += 2
        return res


def test(test_name, A, expected_arr):
    res = Solution().sortArrayByParityII(A)
    print(f'res = {res}')
    if res in expected_arr:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    A1 = [4,2,5,7]
    expected_arr1 = [[4,5,2,7], [4,7,2,5], [2,5,4,7], [2,7,4,5]]
    test('test1', A1, expected_arr1)


# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; 
# and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Note:

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
