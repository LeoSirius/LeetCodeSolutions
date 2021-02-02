from typing import *

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2
        setA = set(A)

        res = None
        for y in B:
            x = y + delta
            if x in A:
                return [x, y]

        return res


def test(test_name, A, B, expected):
    res = Solution().fairCandySwap(A, B)
    if res == expected:
        print(test_name + ' success.')


if __name__ == '__main__':
    A1 = [1,1]
    B1 = [2,2]
    expected1 = [1,2]
    test('test1', A1, B1, expected1)

    A2 = [1,2]
    B2 = [2,3]
    expected2 = [1,2]
    test('test2', A2, B2, expected2)

    A3 = [2]
    B3 = [1,3]
    expected3 = [2,3]
    test('test3', A3, B3, expected3)

    A4 = [1,2,5]
    B4 = [2,4]
    expected4 = [5,4]
    test('test4', A4, B4, expected4)


# Alice and Bob have candy bars of different sizes: 
# A[i] is the size of the i-th bar of candy that Alice has, 
# and B[j] is the size of the j-th bar of candy that Bob has.

# Since they are friends, they would like to exchange one candy 
# bar each so that after the exchange, they both have the same 
# total amount of candy.  (The total amount of candy a person 
# has is the sum of the sizes of candy bars they have.)

# Return an integer array ans where ans[0] is the size of the 
# candy bar that Alice must exchange, and ans[1] is the size 
# of the candy bar that Bob must exchange.

# If there are multiple answers, you may return any one of them.  
# It is guaranteed an answer exists.

#  

# Example 1:

# Input: A = [1,1], B = [2,2]
# Output: [1,2]
# Example 2:

# Input: A = [1,2], B = [2,3]
# Output: [1,2]
# Example 3:

# Input: A = [2], B = [1,3]
# Output: [2,3]
# Example 4:

# Input: A = [1,2,5], B = [2,4]
# Output: [5,4]

# Note:

# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# It is guaranteed that Alice and Bob have different total amounts of candy.
# It is guaranteed there exists an answer.
